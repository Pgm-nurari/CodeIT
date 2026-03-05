var fs = require("fs");

fs.readFile(
    'inputfile2.txt', 
    function(ferr,data){
        if(ferr) return console.error(ferr);
        console.log(data.toString());
});

console.log("Execution Ends")