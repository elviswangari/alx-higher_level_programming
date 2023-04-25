#!/usr/bin/node
/* a script to write to a file */

const file = process.argv[2];
const filedata = process.argv[3];
const fs = require('fs');

const data = Buffer.alloc(filedata.length, filedata, 'UTF8');
fs.writeFileSync(file, data);
