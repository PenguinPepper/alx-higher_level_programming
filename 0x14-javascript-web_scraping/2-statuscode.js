#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, response, body) {
 // console.error('errir: ', err);
  console.log('code:', response && response.statusCode);
  //console.log('body:', body);
});
