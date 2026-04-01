const express = require('express');
const app = express();

// Application level Middleware to log the request method and URL
app.use((req, res, next) => {
    console.log(`Request Recieved`);
    next(); // Call the next middleware or route handler
});

// Route to handle GET requests to the root URL
app.get('/', (req, res) => {
    res.send('Welcome to Home Page - Application Level Middleware');
});

// Start the server
app.listen(3000, () => {
    console.log('Server is running on port 3000');
});