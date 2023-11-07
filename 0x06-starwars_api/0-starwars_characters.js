#!/usr/bin/node

const axios = require('axios');

const getCharacters = async (movieId) => {
  try {
    // Fetch the film data from SWAPI
    const filmResponse = await axios.get(`https://swapi.dev/api/films/${movieId}/`);
    const characterUrls = filmResponse.data.characters;

    // Fetch each character data in series
    for (const url of characterUrls) {
      const characterResponse = await axios.get(url);
      console.log(characterResponse.data.name);
    }
  } catch (error) {
    console.error('Error fetching data: ', error);
  }
};

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];
if (!movieId) {
  console.error('Please provide a Movie ID as the first positional argument.');
  process.exit(1);
}

getCharacters(movieId);
