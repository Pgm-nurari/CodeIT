/*
Deleting A Record : 08/04/2026
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

// Delete Student detail for {rollno : 103}
const deleteStudent = async () => {
  const result = await Student.deleteOne(
    { rollno: 103 }
  )
    .then(() => console.log("Student data deleted successfully"))
    .catch((err) => console.error("Error deleting student", err));
  console.log("Delete Result:", result);
};

deleteStudent();