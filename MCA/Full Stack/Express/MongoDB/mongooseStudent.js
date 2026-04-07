/*
MOngoDB started on - 01/-4/2026
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

// Insert a student records
const insertStudents = async () => {
    await Student.insertMany([
        { rollno: 1, name: "Alice", course: "MCA", semester: 1, mark: 85 },
        { rollno: 2, name: "Bob", course: "MCA", semester: 1, mark: 90 }
    ]);
    console.log("Students inserted successfully");
};

insertStudents();