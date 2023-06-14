#!/usr/bin/node
// prints the first argv passed

if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
