#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (err, res, body) => {
  if (err) throw err;
  const content = JSON.parse(body);
  console.log(content.title);
});
