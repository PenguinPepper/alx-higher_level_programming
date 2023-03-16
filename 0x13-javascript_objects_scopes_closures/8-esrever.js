#!/usr/bin/node
exports.esrever = function (list) {
  const leng = list.length - 1;
  const empty = [];
  for (let i = leng; i >= 0; i--) {
    empty.push(list[i]);
  }
  return empty;
};
