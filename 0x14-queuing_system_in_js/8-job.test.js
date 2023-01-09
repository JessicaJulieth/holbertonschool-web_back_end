import createPushNotificationsJobs from './8-job.js';
import kue from 'kue';
import expect from 'chai';

let queue = kue.createQueue();


before(function() {
  queue.testMode.enter(true);
});

afterEach(function() {
  queue.testMode.clear();
});

after(function() {
  queue.testMode.exit()
});



it('checks queue type and job object', function() {
  const mockList = [{
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  }];
  createPushNotificationsJobs(mockList, queue);
  expect(queue.testMode.jobs[0].data.phoneNumber).to.equal('4153518780');
  expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
  expect(queue.testMode.jobs[0].data).to.eql({
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  });
});

it('checks queue for 2 objects', function() {
  const mockList = [{
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    },
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    }
  ];

  createPushNotificationsJobs(mockList, queue);
  expect(queue.testMode.jobs.length).to.equal(2);
});
