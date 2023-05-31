#!/usr/bin/node
const request = require('request');
const done = {};
request(process.argv[2], (err, res, body) => {
  if (err) throw err;
  const bodyObj = JSON.parse(body);
  for (let i = 0; i < bodyObj.length; i++) {
    const iam = bodyObj[i].userId;
    if (bodyObj[i].completed === true) {
      done[iam] += 1;
      if (done[iam]) {
        done[iam] += 1;
      } else {
        done[iam] = 1;
      }
    /* for (let j = 0; j < listUser.length; j++) {
      if (listUser[j] === j) {
        task++;
    } */
    }
  }
  console.log(done);
});
