//Promise example
let mypromise = new Promise(function(resolve, reject) {
let success = false;

if(success) {
    resolve("Task Completed");
}
else
{
    reject("Task Failed");
}
});

mypromise
.then(function(result) {
console.log(result);
})
.catch(function(error) {
console.log(error);
})
.finally(function() {
console.log("Promise finished");
});