// length 속성을 가진 타입만 허용
interface Lengthwise {
  length: number;
}

function getLength<T extends Lengthwise>(item: T): number {
  // 구현하세요
  return item.length;
}

// id 속성을 가진 객체에서 id 추출
function extractIds<T extends { id: number }>(items: T[]): number[] {
  // 구현하세요
  return items.map((item) => item.id);
}

// 특정 속성을 가진 객체 필터링
function filterByProperty<T, K extends keyof T>(
  items: T[],
  key: K,
  value: T[K]
): T[] {
  // 구현하세요
  return items.filter((item) => item[key] === value);
}

// 테스트
console.log(getLength('hello')); // 5
console.log(getLength([1, 2, 3])); // 3

const users = [
  { id: 1, name: 'Kim' },
  { id: 2, name: 'Lee' },
];
console.log(extractIds(users)); // [1, 2]

console.log(filterByProperty(users, 'name', 'Kim'));
// [{ id: 1, name: "Kim" }]
