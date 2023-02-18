#!/usr/bin/node
let myArg = [];
if (process.argv.length <= 3) {
  console.log(0);
} else if (process.argv[2] === '-') {
  for (let i = 3; i <= process.argv.length - 1; i += 1) {
    myArg.push(Number(process.argv[i]));
    myArg = myArg.sort((a, b) => b - a);
  }
  console.log(myArg[1]);
} else {
  for (let i = 2; i <= process.argv.length - 1; i += 1) {
    myArg.push(Number(process.argv[i]));
    myArg = myArg.sort((a, b) => b - a);
  }
  console.log(myArg[1]);
}
