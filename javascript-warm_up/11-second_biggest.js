#!/usr/bin/node
let myArg = [];
if (process.argv.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i <= process.argv.length - 1; i += 1) {
    myArg.push(Number(process.argv[i]));
    myNewArg = myArg.sort().reverse();
  }
  console.log(myNewArg[1]);
}
