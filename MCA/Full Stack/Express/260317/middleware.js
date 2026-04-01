const express = require('express');
const app = express();

// Middleware to log the request method and URL
app.use((req, res, next) => {
    console.log(`${req.method} ${req.url}`);
    console.log(`Middleware Executed`);
    next(); // Call the next middleware or route handler
});

// Route to handle GET requests to the root URL
app.get('/', (req, res) => {
    res.send('Hello, World!');
});

// Start the server
app.listen(3000, () => {
    console.log('Server is running on port 3000');
});