#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request(url, (error, response, body) => {
  if (!error) {
    const data = JSON.parse(body);
    const characters = data.characters;
    characters.forEach(characterUrl => {
      request(characterUrl, (err, response, body) => {
        if (!err) {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
      });
    });
  }
});
