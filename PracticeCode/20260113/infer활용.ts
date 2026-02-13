// 함수의 첫 번째 매개변수 타입
type FirstParam<T> = T extends (a: infer U, ...args: any[]) => any ? U : never;

// 생성자의 인스턴스 타입
type InstanceOf<T> = T extends new (...args: any[]) => infer U ? U : never;

// 배열의 마지막 요소 타입
type LastElement<T> = T extends [...infer U, infer V] ? V : never;

// 객체의 값 타입 유니온
type ValueOf<T> = T extends object ? T[keyof T] : never;

// 테스트
type K = FirstParam<(a: string, b: number) => void>; // string
type L = InstanceOf<typeof Date>; // Date
type M = LastElement<[1, 2, 3]>; // 3
type N = ValueOf<{ a: string; b: number }>; // string | number
