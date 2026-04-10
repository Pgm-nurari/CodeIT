/*
Updating the cell using roll_no : 08/04/2026
*/

const mongoose = require("mongoose");

// Connect to MongoDB
mongoose
  .connect("mongodb://localhost:27017/College")
  .then(() => console.log("Connected to MongoDB"))
  .catch((err) => console.error("Could not connect to MongoDB", err));

// Define the Student schema
const studentSchema = new mongoose.Schema({
  rollno: Number,
  name: String,
  course: String,
  semester: Number,
  mark: Number,
});

// Create the Student model
const Student = mongoose.model("students", studentSchema);

// Update for {rollno : 103} , set {course : "MSc CS"}
const updateStudent = async () => {
  const result = await Student.updateOne(
    { rollno: 103 },
    { $set: { course: "MSc CS" } },
  )
    .then(() => console.log("Student updated successfully"))
    .catch((err) => console.error("Error updating student", err));
  console.log("Update Result:", result);
};

updateStudent();
