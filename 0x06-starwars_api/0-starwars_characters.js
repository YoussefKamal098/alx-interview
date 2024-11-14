#!/usr/bin/node
const request = require('request');
const STAR_WARS_API_BASE_URL = 'https://swapi-api.hbtn.io/api';

/**
 * Class representing the interaction with the Star Wars API.
 * Provides methods to fetch movie and character data from the Star Wars API.
 */
class StarWarsAPI {
  /**
   * Creates an instance of StarWarsAPI.
   * @param {string} baseUrl - The base URL for the Star Wars API.
   */
  constructor (baseUrl) {
    this.baseUrl = baseUrl;
  }

  /**
   * Constructs the URL for a specific movie's endpoint.
   * @param {number} movieId - The ID of the movie to retrieve.
   * @returns {string} The URL to the movie's endpoint.
   */
  getMovieEndpoint (movieId) {
    return `${this.baseUrl}/films/${movieId}/`;
  }

  /**
   * Fetches the list of character URLs for a given movie.
   * @param {number} movieId - The ID of the movie to fetch character data for.
   * @returns {Promise<string[]>} A promise that resolves to an array of character URLs.
   */
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

  /**
   * Fetches the name of a character from a character URL.
   * @param {string} characterUrl - The URL of the character to fetch the name for.
   * @returns {Promise<string>} A promise that resolves to the character's name.
   */
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

/**
 * Class representing the Star Wars Characters application.
 * Provides methods to display character names from a specific movie.
 */
class StarWarsCharactersApp {
  /**
   * Creates an instance of StarWarsCharactersApp.
   * @param {StarWarsAPI} api - An instance of the StarWarsAPI class to fetch data from.
   */
  constructor (api) {
    this.api = api;
  }

  /**
   * Displays the characters from a specified movie.
   * Character names can either be displayed one by one or all at once.
   * @param {number | string} movieId - The ID of the movie to fetch character data for.
   * @param {boolean} [allAtOnce=false] - Whether to display all character names at once or one by one.
   */
  async displayCharacters (movieId, allAtOnce = false) {
    try {
      // Fetch the URLs of the movie's characters
      const characterUrls = await this.api.fetchMovieCharacters(movieId);

      // Display the character names in the chosen format
      if (allAtOnce) {
        const names = await this.all(characterUrls, this.api.fetchCharacterName);
        console.log(names.join('\n'));
      } else {
        // Display character names one by one
        for await (const name of this.one_by_one(characterUrls, this.api.fetchCharacterName)) {
          console.log(name);
        }
      }
    } catch (error) {
      console.error(`Error: ${error.message}`);
    }
  }

  /**
   * Fetches all character names at once using Promise.all.
   * @param {string[]} urls - An array of character URLs to fetch the names for.
   * @param {Function} fetchFn - The function to fetch the character names (e.g., fetchCharacterName).
   * @returns {Promise<string[]>} A promise that resolves to an array of character names.
   */
  async all (urls, fetchFn) {
    return await Promise.all(urls.map(url => fetchFn(url)));
  }

  /**
   * Fetches character names one by one using async generators.
   * @param {string[]} urls - An array of character URLs to fetch the names for.
   * @param {Function} fetchFn - The function to fetch the character names (e.g., fetchCharacterName).
   * @returns {AsyncGenerator<string>} An asynchronous generator that yields character names one by one.
   */
  async * one_by_one (urls, fetchFn) {
    for (const url of urls) {
      const name = await fetchFn(url);
      yield name;
    }
  }
}

// Retrieve movie ID from command-line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// Instantiate API and application objects
const api = new StarWarsAPI(STAR_WARS_API_BASE_URL);
const app = new StarWarsCharactersApp(api);

// Display characters for the specified movie ID
app.displayCharacters(movieId);
