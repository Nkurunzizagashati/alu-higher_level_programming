#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (!error) {
    const movies = JSON.parse(body).results;
    console.log(movies.reduce((count, movie) => {
      return movie.characters.find((character) => character.endWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
