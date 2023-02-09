#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const mySign = 'X'.repeat(this.width);
    for (let i = 0; i < this.height; i += 1) {
      console.log(mySign);
    }
  }

  rotate () {
    const myVar = this.width;
    this.width = this.height;
    this.height = myVar;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
