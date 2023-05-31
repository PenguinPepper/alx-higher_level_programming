#!/usr/bin/node
const request = require('request');
const people = [];
request(process.argv[2], (err, res, body) => {
  if (err) throw err;
  const bodyobj = JSON.parse(body);
  for (let i = 0; i < bodyobj.results.length; i++) {
    for (let j = 0; j < bodyobj.results[i].characters.length; j++) {
      if (bodyobj.results[i].characters[j] === 'https://swapi-api.alx-tools.com/api/people/18/') {
        people.push(bodyobj.results[i].characters[j]);
      }
    }
  }
  console.log(people.length);
});
