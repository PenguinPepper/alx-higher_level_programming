#!/usr/bin/node
const num = parseInt(process.argv[2]);
let i;
const letter = 'X';
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (i = 1; i <= num; i++) {
    console.log(letter.repeat(num));
  }
}
