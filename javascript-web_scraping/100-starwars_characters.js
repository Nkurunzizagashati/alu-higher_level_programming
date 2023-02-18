#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request.get(url, (error, response, body) => {
  if (!error) {
    const movie = JSON.parse(body);
    movie.characters.forEach(characterUrl => {
      request.get(characterUrl, (err, response, body) => {
        if (!err) {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  }
});
