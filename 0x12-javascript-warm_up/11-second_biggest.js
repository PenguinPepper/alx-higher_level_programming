#!/usr/bin/node
if (process.argv[3]) {
  const arry = [];
  const leng = process.argv.length - 1;
  for (let i = leng; i > 0; i--) {
    arry.push(process.argv[i]);
  }
  arry.sort();
  console.log(arry[arry.length - 2]);
} else {
  console.log(0);
}
