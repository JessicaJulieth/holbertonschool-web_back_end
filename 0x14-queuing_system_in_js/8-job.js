const kue = require('kue');

function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) throw Error('Jobs is not an array');
  for (let j of jobs) {
    const job = queue.create('push_notification_code_3', j).save(function(err) {
        if (err) console.log(`Notification job ${job.id} failed: ${err}`);
        else console.log(`Notification job created: ${job.id}`);
    });
    job.on('complete', function(res) {
        console.log(`Notification job ${job.id} completed`);
    });
    job.on('failed', function(err) {
        console.log(`Notification job ${job.id} failed: ${err}`);
    });
    job.on('progress', function(progress, data) {
        console.log(`Notification job ${job.id} ${progress}% complete`);
    });
    }
}

module.exports = createPushNotificationsJobs;