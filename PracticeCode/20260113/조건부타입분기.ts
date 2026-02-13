// 객체 타입이면 키 목록, 아니면 never
type KeysOf<T> = T extends object ? keyof T : never;

// 배열이면 길이 타입, 아니면 never
type LengthOf<T> = T extends Array<infer U> ? U : never;

// null/undefined 제거
type NonNullable<T> = T extends null | undefined ? never : T;

// 특정 타입만 추출
type Extract<T, U> = T extends U ? T : never;

// 특정 타입 제외
type Exclude<T, U> = T extends U ? never : T;

// 테스트
type G = KeysOf<{ a: number; b: string }>; // "a" | "b"
type H = NonNullable<string | null | undefined>; // string
type I = Extract<'a' | 'b' | 1 | 2, string>; // "a" | "b"
type J = Exclude<'a' | 'b' | 1 | 2, number>; // "a" | "b"
