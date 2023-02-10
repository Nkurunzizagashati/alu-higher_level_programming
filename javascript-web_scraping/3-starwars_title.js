#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;
request.get(url, (response, error) => {
  error
  ? console.error(error)
  : console.log(JSON.parse(response.body).title);
});
