type A = 'a' | 'b' | 'c';
type B = 'b' | 'd';

type R = Extract<A, B>; // "b"

let a: A = 'a';
let b: B = 'b';
let c: R = 'd'; // error "b"만 가능

// ------------------------------------------------------------
function f(x: string | number) {
  if (typeof x === 'string') {
    return x.toUpperCase();
  }
  return x.toFixed(2);
}

function f2(x: string | number): void {
  return;
}

// unknown 타입은 무조건 좁혀서 사용해야함
function parse(input: unknown): unknown {
  if (typeof input === 'string') {
    return input.toUpperCase();
  }

  if (typeof input === 'number') {
    return input.toFixed();
  }

  return input;
}

// 사실상 ts의 기능과 안전성을 포기함
function parse2(input: any): any {
  return input;
}
