type JsonValue =
  | string
  | number
  | boolean
  | null
  | JsonValue[]
  | { [key: string]: JsonValue };

//TODO: 다음 함수들을 구현하세요

// 1. stringify: JsonValue를 문자열로 변환
function stringify(value: JsonValue): string {
  //TODO
  if (typeof value === null) {
    return '';
  }
  if (typeof value === 'string') {
    return value;
  }
  if (typeof value === 'number') {
    return value.toString();
  }
  if (typeof value === 'boolean') {
    return value.toString();
  }
  if (Array.isArray(value)) {
    const items = value.map((v) => stringify(v)).join(',');
    return `[${items}]`;
  }

  if (typeof value === 'object') {
    const entries = Object.entries(value)
      .map(([key, val]) => `"${key}":${stringify(val)}`)
      .join(',');
    return `{${entries}}`;
  }
  return '';
}

// 2. getType: JsonValue의 타입을 문자열로 반환
function getType(value: JsonValue): string {
  //TODO
  if (typeof value === null) {
    return 'null';
  }
  if (typeof value === 'string') {
    return 'string';
  }
  if (typeof value === 'number') {
    return 'number';
  }
  if (typeof value === 'boolean') {
    return 'boolean';
  }
  if (Array.isArray(value)) {
    return 'array';
  }
  if (typeof value === 'object') {
    return 'object';
  }
  return typeof value;
}

// 3. deepClone: JsonValue를 깊은 복사
function deepClone(value: JsonValue): JsonValue {
  //TODO
  if (value === null) {
    return null;
  }
  if (typeof value !== 'object') {
    return value;
  }
  if (Array.isArray(value)) {
    return value.map((item) => deepClone(item));
  }
  const result: { [key: string]: JsonValue } = {};
  for (const key in value) {
    result[key] = deepClone(value[key]);
  }
  return result;
}

// 테스트
console.log(stringify('hello')); // "hello"
console.log(stringify(42)); // "42"
console.log(stringify([1, 2, 3])); // "[1,2,3]"
console.log(stringify({ a: 1 })); // '{"a":1}'

console.log(getType('hello')); // "string"
console.log(getType([1, 2])); // "array"
console.log(getType({ a: 1 })); // "object"
console.log(getType(null)); // "null"
