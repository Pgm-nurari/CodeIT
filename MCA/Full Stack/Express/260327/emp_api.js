const express = require('express');
const app = express();

// Middleware to parse JSON
app.use(express.json());

//Sample employee data
let employees = [
    { id : 1, name : "Anu", department : "HR", salary : 30000},
    { id : 2, name : "Rahul", department : "IT", salary : 45000}
];

// GET - Display all employees
app.get('/employees',(req,res)=>{
    res.json(employees);
});

// GET - Display employee by id
app.get('/employees/:id',(req,res)=>{
    const id = parseInt(req.params.id);
    const employee = employees.find(e => e.id === id);
    if(!employee){
        return res.status(404).json({message : "Employee not found"});
    }
    res.json(employee);
});

// POST - Add new employee
app.post('/employees',(req,res)=>{
    const { name, department, salary } = req.body;
    if(!name || !department || !salary){
        return res.status(400).json({message : "All fields are required"});
    }   
    const newEmployee = {
        id : employees.length + 1,
        name,
        department,
        salary
    };
    employees.push(newEmployee);
    res.status(201).json({message : "Employee added successfully", employee : newEmployee});
});

//PUT - Update employee details based on ID
app.put('/employees/:id',(req,res)=>{
    const id = parseInt(req.params.id);
    const employee = employees.find(e => e.id === id);
    if(!employee){
        return res.status(404).json({message : "Employee not found"});
    }
    const { name, department, salary } = req.body;
    if(name) employee.name = name;
    if(department) employee.department = department;
    if(salary) employee.salary = salary;
    res.json({message : "Employee updated successfully", employee});
});

// DELETE - Remove employee based on ID
app.delete('/employees/:id',(req,res)=>{
    const id = parseInt(req.params.id);
    const index = employees.find(e => e.id === id);
    if(index === -1){
        return res.status(404).json({message : "Employee not found"});
    }
    employees = employees.filter(e => e.id !== id);
    res.json({message : "Employee deleted successfully"});
});

// start server 
app.listen(3000,()=>{
    console.log("Employee API is running on port 3000");
    console.log("Access the API at http://localhost:3000/employees");
});