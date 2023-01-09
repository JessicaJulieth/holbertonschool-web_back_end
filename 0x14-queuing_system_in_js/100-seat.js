const express = require('express');
const kue = require('kue');
const redis = require("redis");
const util = require('util')

const queue = kue.createQueue()

const client = redis.createClient();
const get = util.promisify(client.get).bind(client);

const app = express()
const port = 1245

reserveSeat(50);

let reservationEnabled = true

function reserveSeat(number) {
  client.set('available_seats', number)
}

async function getCurrentAvailableSeats() {
  return await get('available_seats')
}


app.get('/available_seats', async function(req, res) {
  res.send(JSON.stringify({ "numberOfAvailableSeats": await getCurrentAvailableSeats() }))
})

app.get('/reserve_seat', async function(req, res) {
  if (reservationEnabled === false) {
    res.send(JSON.stringify({ "status": "Reservation are blocked" }))
  }

  try {
    const job = queue.createJob('reserve_seat').save()
    res.send(JSON.stringify({ "status": "Reservation in process" }))
    job.on('complete', () => {
      console.log(`Seat reservation job ${job.id} completed`);
    }).on('failed', (err) => {
      console.log(`Seat reservation job ${job.id} failed: ${err}`);
    })
  } catch (err) {
    res.send(JSON.stringify({ "status": "Reservation failed" }))
  }
})


app.get('/process', function(req, res) {
  res.send(JSON.stringify({ "status": "Queue processing" }))

  queue.process('reserve_seat', async function(job, done) {
    const current = Number(await getCurrentAvailableSeats()) - 1

    if (reservationEnabled) {
      reserveSeat(current)
    } else {
      const err = new Error('Not enough seats available')
      done(err)
    }
    if (current <= 0) {
      reservationEnabled = false
    }
    done()
  })

})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})
