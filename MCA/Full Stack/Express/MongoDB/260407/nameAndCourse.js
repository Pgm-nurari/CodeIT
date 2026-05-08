/*
MOngoDB : Fetching details - 07/-4/2026
*/
const mongoose = require("mongoose");

// Connect to MongoDB
mongoose.connect("mongodb://localhost:27017/College").then(() =>
  console.log("Connected to MongoDB")).catch((err) => console.error("Could not connect to MongoDB", err));

// Define the Student schema
const studentSchema = new mongoose.Schema({
    rollno : Number,
    name : String,
    course : String,
    semester : Number,
    mark : Number
});

// Create the Student model
const Student = mongoose.model("students", studentSchema);

// Fetch all student name and course details
Student.find({}, { name: 1, course: 1, _id: 0 }).then((studs) => {
    console.log("Student Name and Course Details : ");
    console.log(studs);
    mongoose.connection.close();
});