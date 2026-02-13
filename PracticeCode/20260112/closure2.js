function makeGreeter(prefix) {
  return function greet(name) {
    return `${prefix} ${name}`;
  };
}

const hello = makeGreeter('hello');
const hi = makeGreeter('hi');

console.log(hello('kim'));
console.log(hi('lee'));
