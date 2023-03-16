#!/usr/bin/node
function getFactorial (num) {
  num = parseInt(process.argv[2]);
  if (num === 0) {
     return(1);
  }
  return (num * getFactorial(num - 1));
}

getFactorial();
