#!/usr/bin/node
let size = Number(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  let row = 'X'.repeat(size);
  for (let i = 0; i < size; i += 1) {
    console.log(row);
  }
}
