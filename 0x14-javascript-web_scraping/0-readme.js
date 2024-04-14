#!/usr/bin/node
const fs = require('fs');

// check if the file is passed as an argument to our script
if (process.argv.length < 3) {
  console.error('Usage: 0-readme.js <filepath>');
  process.exit(1);
}

// load the file from the argument
const filepath = process.argv[2];

// read the file asynchronously
fs.readFileSync(filepath, 'utf-8', (err, data) => {
  if (err) {
    console.error('Error:', err);
    process.exit(1);
  }
  // if no error encounterd print the file
  console.log(data);
});
