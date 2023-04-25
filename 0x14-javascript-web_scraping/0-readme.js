#!/usr/bin/node
/* a script that reads files */
const fs = require('fs');
const file = process.argv[2];
const data = fs.readFileSync(file, 'UTF8');
console.log(data);
