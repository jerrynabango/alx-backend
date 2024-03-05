#!/usr/bin/node
import { createQueue } from "kue";

const queue = createQueue();
const jobData = { phoneNumber: "+254 712345678", message: "Code verification" };

const job = queue
  .create("push_notification_code", jobData)
  .save((err) => {
    if (!err) console.log(`Notification job created: ${job.id}`);
  });

job.on("complete", (result) => {
  console.log("Notification job completed");
});

job.on("failed", (err) => {
  console.log("Notification job failed");
});
