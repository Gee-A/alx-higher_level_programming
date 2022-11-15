#!/usr/bin/node
const request = require('request');
request.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (res.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else if (err) {
    console.log(err);
  }
});
