const file = require('./fileManagement.js');

//Create 
file.createFile('sample.txt')

//write
file.writeFile('sample.txt',"Helloworld\n");

//append
file.appendFile("sample.txt", "This is appended text\n");

//Delete
//file.deleteFile("sample.txt");