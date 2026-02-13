const promise = new Promise((resolve, reject) => {
  // todo: 50%
  //  "Success! Chain1"
  //  "Failed" 즉시
  if (Math.random() < 0.5) {
    setTimeout(() => resolve('Success!'), 3000);
  } else {
    reject(new Error('Failed!'));
  }
});

// 테스트
promise
  .then((value) => {
    console.log(value); // "Success!"
    return value + ' Chain1';
  })
  .then((value) => {
    console.log(value); // "Success! Chain1"
  })
  .catch((e) => console.log(e.message)); // "Failed"

//----------------------------------------------------
// 재사용 테스트
function makePromise() {
  return new Promise((resolve, reject) => {
    if (Math.random() < 0.5) {
      setTimeout(() => resolve('Success!'), 3000);
    } else {
      reject(new Error('Failed!'));
    }
  });
}

for (let i = 0; i < 5; i++) {
  makePromise()
    .then((value) => {
      console.log(value);
    })
    .catch((e) => console.log(e.message));
}
