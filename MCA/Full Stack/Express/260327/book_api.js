const express=require('express');
const app= express();

//middleware to parse JSON 
app.use(express.json());

//sample books data
let books=[
    {id:1,title:"java programming",author:"herbertSchildt"},
    {id:2,title:"python basics ",author:"giudo van ranssom"},

];

//get all books
app.get('/books',(req,res)=>{
    res.json(books);
});

//get book by id
app.get('/books/:id',(req,res)=>{
    const id=parseInt(req.params.id);
    const book=books.find(b=>b.id===id);
    if(!book){
        return res.status(404).json({message : "book not found"});
    }
    res.json(book);
});

//POST -Add a new book
app.post('/books',(req,res)=>{
    const newBook={
        id:books.length+1,
        title:req.body.title,
        author:req.body.author,
    };
    books.push(newBook);
    res.status(201).json(newBook);
});

//PUT- update a book by id
app.put('/books/:id',(req,res)=>{
    const id=parseInt(req.params.id);
    const book=books.find(b=>b.id===id);
    if(!book){
        return res.status(404).json({message:"Book not found"});
    }
    book.title=req.body.title;
    book.author=req.body.author;
    res.json(book);
});

//DELETE - Delete a book
app.delete('/books/:id',(req,res)=>{
    const id=parseInt(req.params.id);
    const book=books.find(b=>b.id===id);
    if(!book){
        return res.status(404).json({message:"Book not found"});
    }
    books = books.filter(b=>b.id!==id);
    res.send("book deleted successfully");
});

// start server 
app.listen(3000,()=>{
    console.log("Book API is running on port 3000");
    console.log("Access the API at http://localhost:3000/books");
});