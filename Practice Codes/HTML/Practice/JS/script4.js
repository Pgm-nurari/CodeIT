/*
Let's learn the use of template literals.
*/

let x=10
let y=11
let z=x+y
//Don't use this:
console.log("The result of x + y is z");
console.log("The result of " + x + " and " + y + " is " +z)
// Instead use the backtick (`) :
console.log(`The sum of ${x} and ${y} is: ${z}`)

//Don't use this:
console.log("The result of \n x + y is z");

// Instead use the backtick (`) :
console.log(`The result of 
 x + y is z`)