//Basic await and async functions
async function example() {
  return "Hello Async!";
}
example().then(res5 => {
  console.log(res5);
});





//function invoke
async function demo() {
  let result = await "Hello Prince!";
  console.log(result);
}
demo();




//async() and wait() with promise
async function ABC() {

  let promise = new Promise((resolve) => {
    setTimeout(() => {
      resolve("Data received successfully!");
    }, 1000);
  });

  let result = await promise;
  console.log(result);
}
ABC();





//async and await promise -resolve & -reject condition with out builtin function
function checkNumber(num) {
  return new Promise((resolve, reject) => {
    if(num > 0) {
      resolve("Number is Positive");
    } else {
      reject("Number is Not Positive");
    }
  });
}

async function runCheck() {
  try {
    let result = await checkNumber(5);
    console.log(result);
  } catch(error) {
    console.log(error);
  }
}
runCheck();



//Basic await and async function
async function example() {
  return "Hello Async!";
}
example().then(result => {
  console.log(result);
});





//function invoke
async function demo() {
  let result = await "Hello Prince!";
  console.log(result);
}
demo();




//async() and wait() with promise
async function ABC() {

  let promise = new Promise((resolve) => {
    setTimeout(() => {
      resolve("Data received successfully!");
    }, 1000);
  });

  let result = await promise;
  console.log(result);
}
ABC();





//async and await promise -resolve & -reject condition with out builtin function
function checkNumber(num) {
  return new Promise((resolve, reject) => {
    if(num > 0) {
      resolve("Number is Positive ");
    } else {
      reject("Number is Not Positive ");
    }
  });
}

async function runCheck() {
  try {
    let result = await checkNumber(5);
    console.log(result);
  } catch(error) {
    console.log(error);
  }
}
runCheck();

