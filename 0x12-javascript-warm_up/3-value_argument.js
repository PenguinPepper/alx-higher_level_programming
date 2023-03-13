#!/usr/bin/node
let print = 1;
if (process.argv.length < 3) {
  console.log('No argument');
} else {
  print = process.argv[2];
  console.log(print);
}
