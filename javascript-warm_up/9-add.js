#!/usr/bin/node
const a = Number(process.argv[2]);
const b = Number(process.argv[3]);
function add (a, b) {
  if (isNaN(Number(process.argv[2])) || isNaN(Number(process.argv[3]))) {
    console.log('NaN');
  } else {
    console.log(a + b);
  }
}
add(parseInt(a), parseInt(b));
