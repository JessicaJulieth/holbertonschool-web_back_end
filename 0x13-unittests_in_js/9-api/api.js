const express = require('express')
const app = express()

app.listen(7865, function() {
  console.log('API available on localhost port 7865');
});

app.get('/', function(req, res) {
  res.send('Welcome to the payment system');
})

app.get('/cart/:id', function(req, res) {
  const id = req.params.id;
  if (!(isNaN(Number(id)))) {
    res.send(`Payment methods for cart ${id}`);
  }
  res.sendStatus(404).end();
})
