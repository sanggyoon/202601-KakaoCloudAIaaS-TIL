// 두 값을 쌍으로 묶기
function makePair<T, U>(first: T, second: U): [T, U] {
  // 구현하세요
  return [first, second];
}

// 쌍의 순서 바꾸기
function swap<T, U>(pair: [T, U]): [U, T] {
  // 구현하세요
  return [pair[1], pair[0]];
}

// 쌍 배열을 객체로 변환
function fromPairs<K extends string | number, V>(
  pairs: [K, V][]
): Record<K, V> {
  // 구현하세요
  const result: Record<K, V> = {} as Record<K, V>;
  for (const [key, value] of pairs) {
    result[key] = value;
  }
  return result;
}

// 테스트
const pair = makePair('name', 42); // ["name", 42]
const swapped = swap(pair); // [42, "name"]
const obj = fromPairs([
  ['a', 1],
  ['b', 2],
]); // { a: 1, b: 2 }
