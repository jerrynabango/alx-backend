function createPushNotificationsJobs(jobs, queue) {
  if (!(jobs instanceof Array)) {
    throw new Error("Jobs is not an array");
  }
  for (let job of jobs) {
    job = queue.create("push_notification_code_3", job);
    job
      .on("complete", (result) => { /* eslint-disable-line no-unused-vars */
        console.log(`Notification job ${job.id} has been completed`);
      })
      .on("failed", (err) => {
        console.log(`Notification job ${job.id} has failed: ${err.message || err.toString()}`);
      })
      .on("progress", (progress, data) => {
        console.log(`Notification job ${job.id} is ${progress}% complete`);
      })
      .save((err) => {
        console.log(`Notification job created: ${job.id}`);
      });
  }
}

module.exports = createPushNotificationsJobs;
