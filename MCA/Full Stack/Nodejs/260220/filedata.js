const fs = require('fs');

const filedata = fs.readFileSync('inputfile1.txt');
console.log(filedata.toString());
console.log("End of program execution.");