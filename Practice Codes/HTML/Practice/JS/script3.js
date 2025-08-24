/*
Conditional statements:
if (condition) { statement }
else if (condition) { statement }
else { statement }
*/

// Using ternary operators ? and :

let x=10
let res = x%2===0 ? "Even" : "Odd" // Store 'Even' or 'Odd' if x%2 is 0
console.log("The result is : ",res)

/*
In Javascript :
1.  = means assignment
2.  == means check if same but exempt the datatype of the value. 
3.  === means check if same and the datatypes match or not.

See example below...
*/

let s=10
console.log("Checking if s==\"10\" : ",s=="10")
console.log("Checking if s===\"10\" : ",s==="10")
