// 깊은 Readonly
type DeepReadonly<T> = {
  readonly [K in keyof T]: T[K] extends object ? DeepReadonly<T[K]> : T[K];
};

// 깊은 Partial
type DeepPartial<T> = {
  [K in keyof T]?: T[K] extends object ? DeepPartial<T[K]> : T[K];
};

// 깊은 Required
type DeepRequired<T> = {
  [K in keyof T]-?: T[K] extends object ? DeepRequired<T[K]> : T[K];
};

// 중첩 객체 평탄화 (키는 점 표기법)
type FlattenObject<T, P extends string = ''> = {
  [K in keyof T]: T[K] extends object
    ? FlattenObject<T[K], `${P}${P extends '' ? '' : '.'}${K & string}`>
    : { [Key in `${P}${P extends '' ? '' : '.'}${K & string}`]: T[K] };
}[keyof T];

// 테스트
type Nested = {
  a: {
    b: {
      c: number;
    };
    d: string;
  };
  e: boolean;
};

type H = DeepReadonly<Nested>;
// 모든 중첩 속성이 readonly

type I = FlattenObject<Nested>;
// { "a.b.c": number; "a.d": string; e: boolean }
