#!/usr/bin/node
exports.esrever = function (list) {
  let myNewList = [];
  for (let i = list.length - 1; i >= 0; i -= 1) {
    myNewList.push(list[i]);
  }
  return myNewList;
}
