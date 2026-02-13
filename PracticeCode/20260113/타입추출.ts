// 배열이면 요소 타입, 아니면 그대로
type Flatten<T> = T extends Array<infer U> ? U : T;

// Promise면 내부 타입, 아니면 그대로
type MyAwaited<T> = T extends Promise<infer U> ? MyAwaited<U> : T;

// 함수면 반환 타입, 아니면 never
type ReturnTypeOf<T> = T extends (...args: any[]) => infer R ? R : never;

// 함수면 매개변수 타입 튜플, 아니면 never
type ParametersOf<T> = T extends (...args: infer P) => any ? P : never;

// 테스트
type A = Flatten<number[]>; // number
type B = Flatten<string>; // string
type C = MyAwaited<Promise<number>>; // number
type D = MyAwaited<Promise<Promise<string>>>; // string
type E = ReturnTypeOf<() => boolean>; // boolean
type F = ParametersOf<(a: string, b: number) => void>; // [string, number]
