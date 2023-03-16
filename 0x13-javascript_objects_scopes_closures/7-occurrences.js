#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let num = 0;
  list.forEach((item) => (item === searchElement && num++));
  return num;
}
