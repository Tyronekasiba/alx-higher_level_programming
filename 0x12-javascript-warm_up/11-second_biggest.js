#!/usr/bin/node

// search the biggest number
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const myVar = process.argv.slice(2).map(Number);
  const secondVar = myVar.sort(function (a, b) { return b - a; })[1];
  console.log(secondVar);
}
