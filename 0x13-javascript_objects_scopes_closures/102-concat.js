#!/usr/bin/node

const fs = require('fs');

const contentA = fs.readFileSync(process.argv[2]).toString();
const contentB = fs.readFileSync(process.argv[3]).toString();

fs.writeFileSync(process.argv[4], contentA.concat(contentB));
