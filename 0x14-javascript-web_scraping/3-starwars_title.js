#!/usr/bin/node
const request = require('request');
const search = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(search, function (err, response, body) {
  if (err) throw err;
  const text = JSON.parse(body);
  console.log(text.title);
});
