type A = {
  name: string;
  age: number;
};

type B = {
  name: string;
  email: string;
};

let user1: A | B = {
  name: 'kim',
  age: 30,
};
let user2: A & B = {
  name: 'lee',
  age: 20,
  email: 'lee@example.com',
};
