//js function
function square(a) {
  return a * a;
}
console.log(square(5));



//add 2 numbers using regular function
function add(a, b) {
return a + b;
}
let result = add(10, 5);
console.log("Sum =", result);



//function passing another function as an argument
function ABC(name){
  return "Hello " + name;
}
function display(func){
  console.log(func("KING"));
}
display(ABC);



//Function returning other function
function outer() {
  return function inner() {
    console.log("Function1 Executed");
  }
}
let fn = outer();
fn();



//MAP func in HOF (double the numbers)
const numbers = [1, 2, 3, 4];
const double = numbers.map(x => x * x);
console.log(double);



//Filter func in HOF (find even)
const num = [1,2,3,4,5,6,7,8,9]
const evens = num.filter(x => x % 2 === 0);
console.log(evens);


//reduce func in HOF ()
const number = [1,2,3,4];
const total = number.reduce((x, y) => x + y);
console.log(total);



//slice with string
let text = "Hello World";
let XYZ = text.slice(0, 5);
console.log(XYZ);


//slice with numbers (array)
let num2 = [10, 20, 30, 40, 50];
let part = num2.slice(1, 4);
console.log(part);



//split with space (string)
let sentence = "JavaScript is Beautiful";
let words = sentence.split(" ");
console.log(words);



//split with comma (string)
let items = "bmw, supra, hyundai";
let res1 = items.split(",");
console.log(res1);



//sort basic
let num3 = [7, 2, 5, 3];
console.log(num3.sort());



//sort ascending
let num4 = [7, 2, 5, 4];

num4.sort(function(a, b) {
  return a - b;
});
console.log(num4);



//sort descending
let num5 = [7, 2, 5, 4];

num5.sort(function(a, b) {
  return b - a;
});
console.log(num5);
