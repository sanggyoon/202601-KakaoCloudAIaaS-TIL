// 타입 정의 없음 (any)
function first(arr: any[]) {
  return arr[0];
}

// 제네릭
// <T>라는 제네릭 파라미터, arr는 T라는 타입으로 이루어짐, 반환 타입은 T
function second<T>(arr: T[]): T | undefined {
  return arr[0];
}

function stringToLength<T>(str: T extends string ? string : T): number | T {
  if (typeof str === 'string') {
    return str.length;
  }
  return str;
}
let abc = 'abc' as const;
