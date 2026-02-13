// 튜플 뒤집기
type Reverse<T extends any[]> = T extends [infer First, ...infer Rest]
  ? [...Reverse<Rest>, First]
  : [];

// 튜플에서 특정 타입 제거
type FilterOut<T extends any[], U> = T extends [infer First, ...infer Rest]
  ? [First] extends [U]
    ? FilterOut<Rest, U>
    : [First, ...FilterOut<Rest, U>]
  : [];

// 두 튜플 합치기
type Concat<T extends any[], U extends any[]> = [...T, ...U];

// 튜플 평탄화
type Flatten<T extends any[]> = T extends [infer First, ...infer Rest]
  ? First extends any[]
    ? [...First, ...Flatten<Rest>]
    : [First, ...Flatten<Rest>]
  : [];

// 테스트
type D = Reverse<[1, 2, 3]>; // [3, 2, 1]
type E = FilterOut<[1, 'a', 2, 'b'], string>; // [1, 2]
type F = Concat<[1, 2], [3, 4]>; // [1, 2, 3, 4]
type G = Flatten<[1, [2, 3], [4]]>; // [1, 2, 3, 4]
