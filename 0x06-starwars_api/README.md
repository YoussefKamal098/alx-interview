# Star Wars Characters API Project

## Overview

The **Star Wars Characters API Project** is a JavaScript-based command-line application designed to fetch and display character names from the Star Wars universe. This is achieved by interacting with an external API to retrieve characters for a specific movie, as identified by the movie ID provided as an argument. The project demonstrates your understanding of API integration, asynchronous programming, and command-line interfaces in Node.js.

## Project Details

### Required Skills and Concepts

To complete this project, you should be familiar with:

1. **HTTP Requests in JavaScript**
    - Making HTTP requests to external services using Node.js (using modules like `request` or `fetch`).
    - [Guide to HTTP Requests in Node.js](https://www.nodejs.org/)

2. **Working with APIs**
    - Understanding RESTful APIs and interacting with them.
    - Parsing and handling JSON data from APIs.
    - [APIs in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction)

3. **Asynchronous Programming**
    - Managing asynchronous operations using callbacks, promises, and async/await.
    - Handling data from API responses asynchronously.
    - [Asynchronous JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous)

4. **Command Line Arguments in Node.js**
    - Accessing command-line arguments with `process.argv`.
    - [Parsing Command Line Arguments](https://nodejs.dev/en/learn/how-to-read-environment-variables-from-nodejs/)

5. **Array Manipulation and Iteration**
    - Iterating over arrays and manipulating data to format and display character names.
    - [JavaScript Array Methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)

## Requirements

### General Guidelines

- **Editors**: Use `vi`, `vim`, or `emacs`.
- **Environment**: Code will be tested on Ubuntu 20.04 LTS with Node.js v10.14.x.
- **File Standards**:
    - Each file must end with a new line.
    - The first line should be `#!/usr/bin/node`.
    - Code should follow `semistandard` guidelines with semicolons, based on the AirBnB style.
    - All files must be executable.
    - Avoid using `var`; use `let` or `const` instead.
- **File Size**: File length will be checked with `wc`.

### Installation

1. **Install Node.js v10**:

    ```bash
    $ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
    $ sudo apt-get install -y nodejs
    ```

2. **Install `semistandard`**:

    ```bash
    $ sudo npm install semistandard --global
    ```

3. **Install the `request` Module**:

    ```bash
    $ sudo npm install request --global
    $ export NODE_PATH=/usr/lib/node_modules
    ```

## Task: Fetching Star Wars Characters

Write a script to print all characters of a Star Wars movie.

### Instructions

1. **Arguments**:
    - The first positional argument is the Movie ID (e.g., `3` for "Return of the Jedi").

2. **Output**:
    - Print one character name per line, in the order they appear in the `characters` list from the `/films/` endpoint.

3. **Requirements**:
    - Use the Star Wars API.
    - Use the `request` module.

### Example

```bash
$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
```

## Repository Structure

- **Repository**: `alx-interview`
- **Directory**: `0x06-starwars_api`
- **File**: `0-starwars_characters.js`

---

By familiarizing yourself with HTTP requests, asynchronous programming, and API interaction in JavaScript, you’ll be equipped to fetch and display Star Wars characters efficiently.