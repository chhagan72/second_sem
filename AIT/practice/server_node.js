// Import the http core module
const http = require('http');

// Define the hostname and port
const hostname = '127.0.0.1';
const port = 3000;

// Create the HTTP server
const server = http.createServer((req, res) => {
  // Set the response header with a status code and content type
  // res.statusCode = 200;
  res.setHeader('Content-Type', 'text/html');

  // Write the HTML response
  res.write(`
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Node.js Web Server</title>
      <style>
        body {
          font-family: Arial, sans-serif;
          text-align: center;
          padding: 50px;
        }
        h1 {
          color: #333;
        }
        p {
          font-size: 1.2em;
        }
      </style>
    </head>
    <body>
      <h1>Welcome to My Node.js Server</h1>
      <p>This is a simple web page served by a Node.js server.</p>
    </body>
    </html>
  `);

  // End the response
  res.end();
});

// Make the server listen on the defined port and hostname
server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
