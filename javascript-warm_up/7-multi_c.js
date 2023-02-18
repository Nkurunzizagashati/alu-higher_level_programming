#!/usr/bin/node
if (isNaN(Number(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < Number(process.argv[2]); i += 1) {
    console.log('C is fun');
  }
}
