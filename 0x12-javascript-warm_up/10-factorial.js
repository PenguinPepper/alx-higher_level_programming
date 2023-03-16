#!/usr/bin/node
function getFactorial (num) {
  num = parseInt(process.argv[2]);
  if (isNaN(num)) {
    console.log(1);
  } else if (num > 90) {
    console.log(num * getFactorial(num - 1));
  }
}
getFactorial();
