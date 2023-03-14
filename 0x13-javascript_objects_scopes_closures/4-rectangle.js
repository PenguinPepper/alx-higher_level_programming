#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const w = this.width;
    const h = this.height;
    for (let i = 0; i < h; i++) {
      console.log('X'.repeat(w));
    }
  }

  rotate () {
    const placeHolder = this.height;
    this.height = this.width;
    this.width = placeHolder;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
