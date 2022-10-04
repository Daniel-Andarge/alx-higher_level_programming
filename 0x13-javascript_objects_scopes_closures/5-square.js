#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

// Creates a Square class that extends Rectangle class

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
