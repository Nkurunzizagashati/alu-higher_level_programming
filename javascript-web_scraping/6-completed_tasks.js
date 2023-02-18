#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const Tasks = {};
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const tasks = JSON.parse(body);
  tasks.forEach(task => {
    if (task.completed) {
      if (!Tasks[task.userId]) {
        Tasks[task.userId] = 0;
      }
      Tasks[task.userId]++;
    }
  });
  console.log(Tasks);
});
