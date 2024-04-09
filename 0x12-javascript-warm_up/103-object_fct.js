#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12,
  incr() {
    this.value++;
  }
};

console.log(myObject); // Output: { type: 'object', value: 12 }

myObject.incr();
console.log(myObject); // Output: { type: 'object', value: 13 }

myObject.incr();
console.log(myObject); // Output: { type: 'object', value: 14 }

myObject.incr();
console.log(myObject); // Output: { type: 'object', value: 15 }
