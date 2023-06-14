#!/usr/bin/node
// prints x times “C is fun”
const myVar = parseInt(process.argv[2]);
if (isNaN(myVar)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myVar; i++) {
    console.log('C is fun');
  }
}
