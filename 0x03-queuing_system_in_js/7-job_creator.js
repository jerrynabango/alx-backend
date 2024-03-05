import { createQueue } from 'kue';

const queue = createQueue();

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'Verification code 1234 is sent for account verification',
  },
  {
    phoneNumber: '4153518781',
    message: 'Verification code 4562 is sent for account verification',
  },
  {
    phoneNumber: '4153518743',
    message: 'Verification code 4321 is sent for account verification',
  },
  {
    phoneNumber: '4153538781',
    message: 'Verification code 4562 is sent for account verification',
  },
  {
    phoneNumber: '4153118782',
    message: 'Verification code 4321 is sent for account verification',
  },
  {
    phoneNumber: '4153718781',
    message: 'Verification code 4562 is sent for account verification',
  },
  {
    phoneNumber: '4159518782',
    message: 'Verification code 4321 is sent for account verification',
  },
  {
    phoneNumber: '4158718781',
    message: 'Verification code 4562 is sent for account verification',
  },
  {
    phoneNumber: '4153818782',
    message: 'Verification code 4321 is sent for account verification',
  },
  {
    phoneNumber: '4154318781',
    message: 'Verification code 4562 is sent for account verification',
  },
  {
    phoneNumber: '4151218782',
    message: 'Verification code 4321 is sent for account verification',
  },
];

for (let job of jobs) {
  const createdJob = queue.create("push_notification_code_2", job);
  createdJob
    .on("complete", (result) => {
      console.log(`Notification job ${createdJob.id} completed`);
    })
    .on("failed", (err) => {
      console.log(`Notification job ${createdJob.id} failed: ${err.message || err.toString()}`);
    })
    .on("progress", (progress, data) => {
      console.log(`Notification job ${createdJob.id} ${progress}% complete`);
    })
    .save((err) => {
      console.log(`Notification job created: ${createdJob.id}`);
    });
}
