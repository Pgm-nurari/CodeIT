const express = require('express');
const app = express();

// Route to read the query parameter and respond with a message
app.get('/search', (req, res) => {
    const name = req.query.name; // Get the 'name' query parameter
    const age = req.query.age;   // Get the 'age' query parameter

    res.send(`Hello ${name}, you are ${age} years old!`); // Respond with a message
});

// Start the server
app.listen(3000, () => {
    console.log('Server is running on port 3000');
});