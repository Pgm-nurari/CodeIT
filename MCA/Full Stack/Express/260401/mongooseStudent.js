const mongoose = require('mongoose');

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/College')
  .then(() => console.log('Connected to MongoDB'))
  .catch(err => console.error('Could not connect to MongoDB', err));

// Define the Student schema
const studentSchema = new mongoose.Schema({
  rollno: Number,
  name: String,
  course: String,
  semester : Number,
  mark: Number
});

// Creating the Students model
const Students = mongoose.model('students', studentSchema);

// Insert Student Records
const insertStudents = async () => {
  const studentsRecords = [
    { rollno: 111, name: 'Alice', course: 'MCA', semester: 1, mark: 85 },
    { rollno: 112, name: 'Bob', course: 'MCA', semester: 1, mark: 78 },
    { rollno: 113, name: 'Charlie', course: 'MCA', semester: 1, mark: 92 },
    { rollno: 114, name: 'David', course: 'MCA', semester: 1, mark: 88 },
    { rollno: 115, name: 'Eve', course: 'MCA', semester: 1, mark: 80 }
  ];
  try {
    await Students.insertMany(studentsRecords);
    console.log('Students inserted successfully');
  } catch (err) {
    console.error('Error inserting students:', err);
  }
};

// Call the function to insert students
insertStudents();