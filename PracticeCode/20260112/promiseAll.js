const p1 = fetch('https://jsonplaceholder.typicode.com/todos/1').then((e) =>
  e.json()
);
const p2 = fetch('https://jsonplaceholder.typicode.com/todos/2').then((e) =>
  e.json()
);
const p3 = fetch('https://jsonplaceholder.typicode.com/todos/3').then((e) =>
  e.json()
);

// 동기 프로그램
console.time('sync');
// [p1, p2, p3].map((p) => p.then(console.log));
console.time('p1');
await p1;
console.timeEnd('p1');
console.time('p2');
await p2;
console.timeEnd('p2');
console.time('p3');
await p3;
console.timeEnd('p3');
console.timeEnd('sync');

// todo: Promise.all 활용 구현
console.time('async');
Promise.allSettled([p1, p2, p3])
  .then((values) => {
    console.log(values);
  })
  .catch((e) => {
    console.log(e.message);
  });
console.timeEnd('async');
