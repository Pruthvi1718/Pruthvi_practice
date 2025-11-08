//Ex1 importing data from module1
import { add, sub } from './module1.js';

console.log(add(10, 5));
console.log(sub(10, 5));
//op will be 10 and 5



//Ex2 default import from module1
import greet from './module1.js';
console.log(greet("ABC"));



//Ex3 real time example
import { login, logout } from "./module1.js";

console.log(login("admin", "1234"));
console.log(logout());



//Ex4 with API fetch
import { getUsers } from "./module1.js";

getUsers().then(users => console.log(users));
