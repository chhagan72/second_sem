// Core Module

    // const http = require('http');
    // const server = http.createServer((req, res)=>{
    //     res.statusCode=200;
    //     res.setHeader('content-Type','text/plain');
    //     res.end('Hello, World!\n');
    // });
    // server.listen(3000,'127.0.0.1',()=>{
    //     console.log('Server running at http://127.0.0.1:3000/');
    // });

// Local Module 
    const math = require('./mod');
    var a = math.add(2,4);
    console.log(a);
   var  b = math.sub(2,1);
    console.log(b);

var c = a+b;
console.log(c)