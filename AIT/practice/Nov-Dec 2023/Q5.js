// Write a program to create a server in NodeJS and display server responses on a web page.

// Import the required modules
const http = require('http');

// Define the port number
const port = 3000;

// Create the server
const server = http.createServer((res) => {
    // Set the response header with content type
    res.writeHead(200, {'Content-Type': 'text/html'});
    
    // Write the HTML content to the response
    res.write('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Document</title><link rel="stylesheet" href="Q2_style.css"></head><body>');
    res.write('<h1>Helo This is my first wweb page.....</h1> <br><p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Velit voluptatem, culpa impedit temporibus facilis cum minima porro adipisci. Numquam placeat architecto doloribus eligendi nostrum animi blanditiis saepe et praesentium ea?</p><div><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhx39OyLb2FaDNEd0rZ8yM6l7EtBscnGqdAw&usqp=CAU" alt="THis is a "></div>');
    res.write('</body></html>');
    
    // End the response
    res.end();
});

// Start the server and listen on the defined port
server.listen(port, () => {
    console.log(`Server running at http://localhost:${port}/`);
});
