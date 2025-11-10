//Promise example
let promise = new Promise(function(resolve, reject) {
let success = true;

if(success) {
    resolve("Task Completed");
}
else
{
    reject("Task Failed");
}
});

promise
.then(function(result) {
console.log(result);
})
.catch(function(error) {
console.log(error);
})
.finally(function() {
console.log("Promise finished");
});



//setTimeout for resolve condition
let promise1 = new Promise(function(resolve, reject) {
let success = true;

if(success) {
    setTimeout(() => {
    resolve("Task Completed");
}, 2000);
}
else
{
    reject("Task Failed");
}
});

promise1
.then(function(result) {
console.log(result);
})
.catch(function(error) {
console.log(error);
})
.finally(function() {
console.log("Promise finished");
});



//setTimeout for reject condition
let promise2 = new Promise(function(resolve, reject) {
let success = false;

if(success) {
    resolve("Task Completed");
}
else
{
    setTimeout(() => {
    reject("Task Failed");
}, 3000);
}
});

promise2
.then(function(result) {
console.log(result);
})
.catch(function(error) {
console.log(error);
})
.finally(function() {
console.log("Promise finished");
});



//setTimeout for Mixed behavior
let promise3 = new Promise(function(resolve, reject) {
let success = true;

if(success) {
    setTimeout(() => {
    resolve("Task Completed");
}, 4000);
}
else
{
    setTimeout(() => {
    reject("Task Failed");
}, 4000);
}
});

promise3
.then(result => console.log(result))
.catch(error => console.log(error))
.finally(() => console.log("Promise finished"));



//wrapping of function & return promise
function Task1(success) {
  return new Promise((resolve, reject) => {

if(success) {
    resolve("Task Completed");
}
else
{
    reject("Task Failed");
}
});
}

Task1(true)
.then(result => console.log(result))
.catch(error => console.log(error))
.finally(() => console.log("Promise finished."));