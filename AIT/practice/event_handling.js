// const EventEmitter = require('events');
// class myEmitter extends EventEmitter{};
// const MyEmitter = new myEmitter();
// MyEmitter.on('great', ()=>{
//     console.log("This is a event handling function in node js")
// });
// MyEmitter.on('great', (name)=>{
//     console.log(`Your name is ${name}`)
// });


// MyEmitter.emit('great');
// MyEmitter.emit('great', 'chhagan');


// multiplication using event handling in node js 

const EventEmitter = require('events');
const ev = new EventEmitter();

ev.on('ck',(x,y)=>{
 console.log(x*y);
});
ev.emit('ck',2,4);
// function multi(x,y){
//     return x*y;

// }

// Mul.on('multiplication',(x,y) =>{
//     const result = multi(x,y)
//     console.log(`The value of X is : ${x} And value of Y is : ${y} And Multiplication of X and Y is : ${result}`);
// });

// Mul.emit('multiplication',5,3);