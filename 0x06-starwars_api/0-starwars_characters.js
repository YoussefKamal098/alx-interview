#!/usr/bin/node
const request = require('request');
const STAR_WARS_API_BASE_URL = 'https://swapi-api.hbtn.io/api';

class StarWarsAPI {
  constructor (baseUrl) {
    this.baseUrl = baseUrl;
  }

  getMovieEndpoint (movieId) {
    return `${this.baseUrl}/films/${movieId}/`;
  }

  fetchMovieCharacters (movieId) {
    return new Promise((resolve, reject) => {
      const url = this.getMovieEndpoint(movieId);

      request(url, { json: true }, (error, response, body) => {
        if (error) {
          return reject(error);
        }

        if (response.statusCode !== 200) {
          return reject(new Error(`Failed to load movie: ${response.statusCode}`));
        }

        resolve(body.characters);
      });
    });
  }

  fetchCharacterName (characterUrl) {
    return new Promise((resolve, reject) => {
      request(characterUrl, { json: true }, (error, response, body) => {
        if (error) {
          return reject(error);
        }

        if (response.statusCode !== 200) {
          return reject(new Error(`Failed to load character: ${response.statusCode}`));
        }

        resolve(body.name);
      });
    });
  }
}

class StarWarsCharactersApp {
  constructor (api) {
    this.api = api;
  }

  async displayCharacters (movieId, allAtOnce = false) {
    try {
      const characterUrls = await this.api.fetchMovieCharacters(movieId);

      if (allAtOnce) {
        const names = await this.all(characterUrls, this.api.fetchCharacterName);
        console.log(names.join('\n'));
      } else {
        for await (const name of this.one_by_one(characterUrls, this.api.fetchCharacterName)) {
          console.log(name);
        }
      }
    } catch (error) {
      console.error(`Error: ${error.message}`);
    }
  }

  async all (urls, fetchFn) {
    return await Promise.all(urls.map(url => fetchFn(url)));
  }

  async * one_by_one (urls, fetchFn) {
    for (const url of urls) {
      const name = await fetchFn(url);
      yield name;
    }
  }
}

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const api = new StarWarsAPI(STAR_WARS_API_BASE_URL);
const app = new StarWarsCharactersApp(api);

app.displayCharacters(movieId, false);
