// 에러 1
const user: {
  name: string;
  age: number;
  email?: string;
} = {
  name: 'Kim',
  age: 25,
};

user.email = 'kim@test.com'; // ✔ OK

// 에러 2
function double(value: number) {
  return value * 2;
}

// 에러 3
const numbers: (number | string)[] = [1, 2, 3];
numbers.push('four');

// 에러 4
function greet(name: string, age?: number) {
  return `Hello,${name}. You are${age} years old.`;
}
greet('Kim');

// 에러 5
const config: {
  port: number | string;
  host: string;
} = {
  port: 3000,
  host: 'localhost',
};
config.port = '3001';
