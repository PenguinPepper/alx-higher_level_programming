#!/usr/bin/node
const fs = require('fs');
const request = require('request');
request(process.argv[2], (err, res, body) => {
  if (err) throw err;
  const text = body;
  fs.writeFile(process.argv[3], text, (error) => {
    if (error) throw error;
  });
});
