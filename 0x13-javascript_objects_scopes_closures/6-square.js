#!/usr/bin/node

const BaseSquare = require('./5-square.js');

class Square extends BaseSquare {
  charPrint (c) {
    if (c) {
      console.log((c.repeat(this.width) + '\n').repeat(this.height - 1) + c.repeat(this.width));
    } else {
      super.print();
    }
  }
}
module.exports = Square;
