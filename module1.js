//Ex1 export data from this file
export const add = (a, b) => a + b;
export const sub = (a, b) => a - b;



//default export from this file
export default function greet(name) {
return `Hello, ${name}`;
}



//ex3 real time example
export function login(username, password) {
  if (username === "admin" && password === "1234") {
    return "Login Successful";
  } else {
    return "Invalid Credentials";
  }
}

export function logout() {
  return "User Logged Out";
}



//Ex4 with API
//Ex4 with API
export async function getUsers() {
const response = await fetch("https://jsonplaceholder.typicode.com/users");
return response.json();
}