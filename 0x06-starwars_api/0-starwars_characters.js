#!/usr/bin/node
const request = require('request');
const pLimit = require('p-limit'); // Install this package
const STAR_WARS_API_BASE_URL = 'https://swapi-api.hbtn.io/api';

/**
 * Lock Manager class that handles lock operations for different processes.
 * It ensures that certain processes are not executed concurrently.
 */
class LockManager {
  constructor () {
    this.locks = new Map(); // A map to store lock statuses for various operations
  }

  /**
   * Check if a given operation is in progress.
   * @param {string} operationName - The name of the operation to check.
   * @returns {boolean} True if the operation is in progress, false otherwise.
   */
  isOperationInProgress (operationName) {
    return !!this.locks.get(operationName); // Return true if the operation is locked
  }

  /**
   * Set the lock for a given operation with a timeout to avoid deadlocks.
   * @param {string} operationName - The name of the operation to lock.
   * @param {number} timeout - The timeout in milliseconds.
   * @returns {Promise<void>} A promise that resolves when the lock is acquired.
   * @throws {Error} If the lock is not acquired within the timeout period.
   */
  async setLock (operationName, timeout = 5000) {
    const startTime = Date.now();

    // If the operation is already locked, wait until it's released or timeout occurs
    while (this.isOperationInProgress(operationName)) {
      if (Date.now() - startTime > timeout) {
        throw new Error(`Timeout: Unable to acquire lock for ${operationName}`);
      }
      await new Promise(resolve => setTimeout(resolve, 100)); // Wait for 100ms before retrying
    }

    this.locks.set(operationName, true); // Lock the operation
  }

  /**
   * Release the lock for a given operation.
   * @param {string} operationName - The name of the operation to release the lock for.
   */
  releaseLock (operationName) {
    if (!this.isOperationInProgress(operationName)) {
      console.warn(`${operationName} is not locked.`);
      return;
    }
    this.locks.delete(operationName); // Release the lock for the operation
  }
}

/**
 * Class representing the interaction with the Star Wars API.
 * Provides methods to fetch movie and character data from the Star Wars API.
 */
class StarWarsAPI {
  constructor (baseUrl) {
    this.baseUrl = baseUrl;
  }

  getMovieEndpoint (movieId) {
    return `${this.baseUrl}/films/${movieId}/`;
  }

  // Fetches the list of character URLs for a given movie with retry and timeout handling
  async fetchMovieCharacters (movieId, retries = 3, timeout = 5000) {
    const url = this.getMovieEndpoint(movieId);
    for (let attempt = 1; attempt <= retries; attempt++) {
      try {
        const body = await this.makeRequest(url, timeout);
        return body.characters;
      } catch (error) {
        if (attempt < retries) {
          console.log(`Retrying... Attempt ${attempt} for movie ${movieId}`);
        } else {
          throw new Error(`Failed to fetch characters after ${retries} retries: ${error.message}`);
        }
      }
    }
  }

  // Fetch a character's name with retry logic
  async fetchCharacterName (characterUrl, retries = 3, timeout = 5000) {
    for (let attempt = 1; attempt <= retries; attempt++) {
      try {
        const body = await this.makeRequest(characterUrl, timeout);
        return body.name;
      } catch (error) {
        if (attempt < retries) {
          console.log(`Retrying... Attempt ${attempt} for character ${characterUrl}`);
        } else {
          throw new Error(`Failed to fetch character: ${error.message}`);
        }
      }
    }
  }

  // Make the actual API request with timeout
  async makeRequest (url, timeout) {
    return new Promise((resolve, reject) => {
      request({ url, json: true, timeout }, (error, response, body) => {
        if (error) {
          return reject(error);
        }
        if (response.statusCode !== 200) {
          return reject(new Error(`Failed with status code ${response.statusCode}`));
        }
        resolve(body);
      });
    });
  }
}

/**
 * Class representing the Star Wars Characters application.
 * Provides methods to display character names from a specific movie.
 */
class StarWarsCharactersApp {
  constructor (api) {
    this.api = api;
    this.lockManager = new LockManager(); // Initialize LockManager instance
    this.limit = pLimit(5); // Limit concurrent API calls to 5 at a time
  }

  async displayCharacters (movieId, allAtOnce = false) {
    const operationName = `fetching-characters-${movieId}`; // Lock for a specific movie

    try {
      await this.lockManager.setLock(operationName);

      // Fetch the URLs of the movie's characters
      const characterUrls = await this.api.fetchMovieCharacters(movieId);

      // Limit the concurrent calls to fetch character names
      if (allAtOnce) {
        const names = await this.all(characterUrls, this.api.fetchCharacterName);
        console.log(names.join('\n'));
      } else {
        for await (const name of this.one_by_one(characterUrls, this.api.fetchCharacterName)) {
          console.log(name);
        }
      }

      this.lockManager.releaseLock(operationName);
    } catch (error) {
      console.error(`Error: ${error.message}`);
    }
  }

  async all (urls, fetchFn) {
    return await Promise.all(urls.map(url => this.limit(() => fetchFn.call(this.api, url))));
  }

  async * one_by_one (urls, fetchFn) {
    for (const url of urls) {
      yield this.limit(() => fetchFn.call(this.api, url));
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
app.displayCharacters(movieId, true);
