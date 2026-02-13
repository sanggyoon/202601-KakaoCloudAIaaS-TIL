const a = 'hello'; // 타입: "hello" literal type
let b = 'hello'; // 타입: string
const c = [1, 2, 3]; // 타입: number[]
const d = [1, 'two', true]; // 타입: (number | string | boolean)[]
const e = { x: 1, y: 2 }; // 타입: { x: number; y: number; }
const f = (x: number) => x * 2; // 타입: (x: number) => number

function g() {
  return { id: 1, name: 'Kim' };
} // 반환 타입: { id: number; name: string; }

const h = [1, 2, 3].map((x) => x.toString()); // 타입: string[]
