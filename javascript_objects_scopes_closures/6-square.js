#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  constructor (size) {
    super(size, size);
  }
  charPrint (c) {
    if (c != undefined) {
      const mySign = c.repeat(this.width);
      for (let i = 0; i < this.height; i += 1) {
        console.log(mySign);
      }
    } else {
      const mySign = 'X'.repeat(this.width);
      for (let i = 0; i < this.height; i += 1) {
        console.log(mySign);
      }
    }
  }
};
