type User5 = {
  id: number;
  name: string;
};

const base: User5 = { id: 1, name: 'kim' };
const ro: Readonly<User5> = base;

ro.name = 'park'; // compile error

base.name = 'Lee'; // OK, mutable 참조
console.log(ro.name); // Lee
