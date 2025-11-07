//JSON with key value pairs EXAMPLES
// {
//   "name": "ABC";
//   "age": 22;
//   "skills": ["JavaScript", "Python", "Node.js"];
// }



//JSON conversions
//JSON.parse(string - object)
let jsonString = '{"name":"XYZ","age":28}';
let user = JSON.parse(jsonString);
console.log(user.name);



//JSON.stringify(object - string)
let student = { name: "PQR", branch: "CS" };
let json = JSON.stringify(student);
console.log(json);



//fetch data with JSON
fetch("https://jsonplaceholder.typicode.com/users")
.then(response => response.json())
.then(data => console.log(data))
.catch(err => console.log("Error:", err));



//JSON with small example
let product = {
id: 101,
name: "Laptop",
price: 50000,
stock: true
};

let jsonData = JSON.stringify(product);
console.log(jsonData);

