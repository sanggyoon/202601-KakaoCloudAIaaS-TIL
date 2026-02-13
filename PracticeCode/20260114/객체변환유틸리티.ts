// 1. 모든 속성을 nullable로
type Nullable<T> = {
  [K in keyof T]: T[K] | null;
};

// 2. 옵셔널 속성만 추출
type OptionalKeys<T> = {
  [K in keyof T]: T[K] extends Required<T>[K] ? never : K;
}[keyof T];
type PickOptional<T> = Pick<T, OptionalKeys<T>>;
// 3. 필수 속성만 추출
type RequiredKeys<T> = {
  [K in keyof T]: T[K] extends Required<T>[K] ? K : never;
}[keyof T];
type PickRequired<T> = Pick<T, RequiredKeys<T>>;

// 4. 두 타입 병합 (후자 우선)
type Merge<T, U> = {
  [K in keyof T | keyof U]: K extends keyof U ? U[K] : T[K];
};
// 5. 두 타입의 차이 (T에만 있는 속성)
type Diff<T, U> = {
  [K in keyof T]: K extends keyof U ? never : K;
}[keyof T];

// 테스트
interface A {
  id: number;
  name?: string;
  email: string;
}

interface B {
  name: string;
  age: number;
}

type OptionalOfA = PickOptional<A>; // { name?: string }
type RequiredOfA = PickRequired<A>; // { id: number; email: string }
type Merged = Merge<A, B>; // { id: number; name: string; email: string; age: number }
type OnlyInA = Diff<A, B>; // { id: number; email: string }
