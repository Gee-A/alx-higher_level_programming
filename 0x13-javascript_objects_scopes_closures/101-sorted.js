#!/usr/bin/node

const { dict } = require('./main.js');

const newDict = Object.entries(dict).reduce((acc, [key, value]) => {
  acc[value] = acc[value] ? [...acc[value], key] : [key];
  return acc;
}, {});
console.log(newDict);
