#!/usr/bin/node
// prints the first argv passed
const numArgv = process.argv
if (process.argv[2]){
	console.log(process.argv[2]);
} else {
	console.log('No argument');
}
