// fileOperations.js
var fs = require('fs');

//Create a file
function createFile(fileName){
    fs.writeFileSync(fileName, " ");
    console.log("File created successfully.");
}

//Write data into file
function writeFile(fileName, data){
    fs.writeFileSync(fileName, data);
    console.log("Data written successfully.");
}

//Append data into file
function appendFile(fileName, data){
    fs.appendFileSync(fileName, data);
    console.log("Data appended successfully.");
}

