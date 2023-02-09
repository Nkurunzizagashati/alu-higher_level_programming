#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let numberOfOccurences = 0;
  for (let i = 0; i < list.length; i += 1) {
    if (list[i] === searchElement) {
      numberOfOccurences += 1;
    }
  }
  return numberOfOccurences;
}
