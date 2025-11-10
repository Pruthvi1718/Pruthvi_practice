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