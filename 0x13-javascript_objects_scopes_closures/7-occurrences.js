#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let num = 0;
  if (list.contains(searchElement)) {
    num++;
  }
  return num;
}
