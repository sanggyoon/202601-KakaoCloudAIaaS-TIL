// 모든 속성을 옵셔널로
type MyPartial<T> = { [K in keyof T]?: T[K] };

// 모든 속성을 필수로
type MyRequired<T> = { [K in keyof T]-?: T[K] };

// 모든 속성을 읽기 전용으로
type MyReadonly<T> = { readonly [K in keyof T]: T[K] };

// 모든 속성 타입을 특정 타입으로 변경
type Record<K extends keyof any, V> = { [P in K]: V };

// 테스트
type User = { name: string; age: number };

type PartialUser = MyPartial<User>;
// { name?: string; age?: number }

type ReadonlyUser = MyReadonly<User>;
// { readonly name: string; readonly age: number }

type StringRecord = Record<'a' | 'b', string>;
// { a: string; b: string }
