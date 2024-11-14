# Node.js `request` Module Guide

This guide covers using the `request` module in Node.js to make HTTP requests, handle JSON data, work with various authentication methods, and stream data.

## Table of Contents
1. [Introduction to the `request` Module](#introduction-to-the-request-module)
2. [Installation](#installation)
3. [Making HTTP Requests](#making-http-requests)
    - [GET Requests with URL Query Parameters](#get-requests-with-url-query-parameters)
    - [POST Requests with JSON Data](#post-requests-with-json-data)
    - [Sending URL-Encoded Form Data](#sending-url-encoded-form-data)
4. [Handling JSON Responses](#handling-json-responses)
5. [Authentication Methods](#authentication-methods)
    - [Basic Authentication](#basic-authentication)
    - [JWT Authentication](#jwt-authentication)
    - [Session-Based Authentication with Cookies](#session-based-authentication-with-cookies)
6. [Streaming Data with `request`](#streaming-data-with-request)

---

## Introduction to the `request` Module

The `request` module simplifies HTTP requests in Node.js. It provides methods to send requests with different HTTP methods (GET, POST, etc.), handle JSON data, work with query parameters, and manage cookies.

## Installation

To install the `request` module, use the following command:

```bash
npm install request
```

## Making HTTP Requests

The `request` module allows you to make HTTP requests with ease. Here are examples of making GET and POST requests with parameters and form data.

### GET Requests with URL Query Parameters

You can add query parameters to the URL using the `qs` option in the request options:

```javascript
const request = require('request');

const options = {
  url: 'https://jsonplaceholder.typicode.com/posts',
  qs: {
    userId: 1,
    limit: 5
  },
  json: true
};

request.get(options, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode === 200) {
    console.log('Response:', body);
  } else {
    console.log('Request failed with status code:', response.statusCode);
  }
});
```

- **`qs`**: An object containing query parameters (e.g., `userId=1` and `limit=5`).
- **`json: true`**: Automatically parses JSON response.

### POST Requests with JSON Data

To send JSON data in a `POST` request, set `json: true` and include the data in the `body` option:

```javascript
const options = {
  url: 'https://jsonplaceholder.typicode.com/posts',
  method: 'POST',
  json: true,
  body: {
    title: 'New Post',
    body: 'This is the content of the new post.',
    userId: 1
  }
};

request(options, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode === 201) {
    console.log('New Post Created:', body);
  } else {
    console.log('Request failed with status code:', response.statusCode);
  }
});
```

- **`json: true`**: Automatically formats the request as JSON.
- **`body`**: Contains JSON data to send in the request.


### Sending URL-Encoded Form Data

To send URL-encoded form data, use the `form` option instead of `body`.

```javascript
const options = {
  url: 'https://example.com/login',
  method: 'POST',
  form: {
    username: 'user',
    password: 'pass'
  }
};

request(options, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode === 200) {
    console.log('Logged in successfully:', body);
  } else {
    console.log('Login failed with status code:', response.statusCode);
  }
});
```

- **`form`**: Formats data as URL-encoded form data, setting `Content-Type` to `application/x-www-form-urlencoded`.

## Handling JSON Responses

To automatically parse JSON responses, use `json: true`. If you prefer manual parsing, simply omit `json: true` and parse `body` with `JSON.parse(body)`.

```javascript
const options = {
  url: 'https://jsonplaceholder.typicode.com/posts/1'
};

request.get(options, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log('Post Data:', data);
  } else {
    console.log('Request failed with status code:', response.statusCode);
  }
});
```

## Authentication Methods

The `request` module supports several authentication methods, such as Basic Authentication, JWT, and session-based cookies.

### Basic Authentication

To use Basic Authentication, include the `Authorization` header with a Base64-encoded `username:password`.

```javascript
const options = {
  url: 'https://api.example.com/protected-endpoint',
  headers: {
    'Authorization': 'Basic ' + Buffer.from('username:password').toString('base64')
  }
};

request.get(options, (error, response, body) => {
  console.log('Response:', body);
});
```

### JWT Authentication

JWT-based authentication requires you to obtain a token and send it in the `Authorization` header for each request.

1. **Login and Obtain JWT**:

```javascript
const options = {
  url: 'https://api.example.com/login',
  method: 'POST',
  json: true,
  body: {
    username: 'user',
    password: 'password'
  }
};

request(options, (error, response, body) => {
  const token = body.token;
});
```

2. **Use JWT for Protected Requests**:

```javascript
const options = {
  url: 'https://api.example.com/protected-endpoint',
  headers: {
    'Authorization': 'Bearer ' + token
  }
};

request.get(options, (error, response, body) => {
  console.log('Protected Data:', body);
});
```

### Session-Based Authentication with Cookies

With session-based authentication, you typically receive a session cookie after logging in.

1. **Login and Store Session Cookie**:

```javascript
const jar = request.jar();
const options = {
  url: 'https://api.example.com/login',
  method: 'POST',
  json: true,
  body: {
    username: 'user',
    password: 'password'
  },
  jar: jar
};

request(options, (error, response) => {
  console.log('Login successful. Cookies stored.');
});
```

2. **Use Session Cookie for Authenticated Requests**:

```javascript
const options = {
  url: 'https://api.example.com/protected-endpoint',
  jar: jar
};

request.get(options, (error, response, body) => {
  console.log('Protected Data:', body);
});
```

- **`jar`**: Stores cookies across requests, allowing session-based authentication.

---

## Streaming Data with `request`

The `request` module can be used to stream large files directly to the file system without loading the entire file into memory. This is especially useful for handling large downloads.

### Example: Downloading an Image Using Streams

In this example, we use `request` to download an image and stream it to the file system using `fs.createWriteStream`.

```javascript
const request = require('request');
const fs = require('fs');

const file = fs.createWriteStream('downloaded_image.jpg');

request('https://via.placeholder.com/150').pipe(file);

file.on('finish', () => {
  console.log('File downloaded successfully');
});

file.on('error', (error) => {
  console.error('Error downloading file:', error);
});
```

- **`pipe`**: Connects the readable stream from the HTTP request to the writable stream (file), reducing memory usage by not loading the entire file into RAM.

---

This README covers essential usage of the `request` module, including making HTTP requests, handling JSON data, performing authentication, and streaming data. For more advanced options, consult the [request module documentation](https://github.com/request/request).