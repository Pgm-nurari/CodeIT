var http = require('http') //require is used to import modules into our program

http.createServer(    //creates an http server
    function(req,res)
    {
        res.write("Welcome")
        res.end()
    }
).listen(8080)


// req -> request object (information sent by the client)
// res -> response object (used to send data back to the client)
// res.write() -> sends data to the client.
// res.end() -> ends the response.
// listen(8080) -> makes the server listen on hthe port 8080

/*
,dnjadhgdhjekje
slbdfhjwefjhew
*/