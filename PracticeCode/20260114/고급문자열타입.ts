// ===== 1. camelCase를 kebab-case로 =====

// type CamelToKebab: 타입 정의
// <S extends string>: S는 string 타입이어야 함
// = S extends `${infer First}${infer Rest}`: S가 "첫글자 + 나머지" 패턴인지 확인
type CamelToKebab<S extends string> = S extends `${infer First}${infer Rest}`
  // ? `${First}${...}`: 매칭되면 변환 시작
  // Rest extends Capitalize<Rest>: Rest가 대문자로 시작하는지 확인
  //   Capitalize<Rest>: Rest의 첫 글자를 대문자로 만든 결과
  //   Rest가 이미 대문자로 시작하면 true (예: "Color"는 "Color"와 같음)
  // ? `-${Lowercase<Rest>}`: 대문자면 앞에 하이픈 추가하고 소문자로 변환
  // : '': 대문자가 아니면 아무것도 추가 안 함
  ? `${First}${Rest extends Capitalize<Rest> ? `-${Lowercase<Rest>}` : ''}`
  // : S: 패턴 매칭 실패하면 원본 그대로
  : S;

// type A: 'backgroundColor'를 변환
// "b" + "ackgroundColor"
// "ackgroundColor"가 Capitalize("ackgroundColor") = "AckgroundColor"와 다름 → '' 추가
// 결과: "b"
// ❌ 이 구현은 잘못됨!
type A = CamelToKebab<'backgroundColor'>; // 실제로는 제대로 작동 안 함

// ===== 올바른 CamelToKebab 구현 =====
type CamelToKebabCorrect<S extends string> = 
  // S extends `${infer First}${infer Rest}`: 첫 글자와 나머지 분리
  S extends `${infer First}${infer Rest}`
    // Rest extends Uncapitalize<Rest>: Rest가 소문자로 시작하는지 확인
    //   Uncapitalize<Rest>: Rest의 첫 글자를 소문자로
    //   같으면 → 소문자로 시작 (camelCase 경계 아님)
    //   다르면 → 대문자로 시작 (camelCase 경계!)
    ? Rest extends Uncapitalize<Rest>
      // 소문자면 그냥 이어서 재귀
      ? `${Lowercase<First>}${CamelToKebabCorrect<Rest>}`
      // 대문자면 하이픈 추가하고 재귀
      : `${Lowercase<First>}-${CamelToKebabCorrect<Rest>}`
    // 더 이상 분리 안 되면 소문자로 변환
    : Lowercase<S>;

// ===== 2. kebab-case를 camelCase로 =====

// type KebabToCamel: 타입 정의
// <S extends string>: S는 string 타입
// = S extends `${infer First}-${infer Rest}`: S가 "앞부분-뒷부분" 패턴인지 확인
//   infer First: 하이픈 앞의 문자열을 First에 저장
//   infer Rest: 하이픈 뒤의 문자열을 Rest에 저장
type KebabToCamel<S extends string> = S extends `${infer First}-${infer Rest}`
  // ? `${First}${Capitalize<KebabToCamel<Rest>>}`: 매칭되면
  //   First: 하이픈 앞 부분 그대로 (예: "background")
  //   KebabToCamel<Rest>: Rest를 재귀적으로 변환 (예: "color")
  //   Capitalize<...>: 변환된 결과의 첫 글자를 대문자로 (예: "Color")
  //   결과: "background" + "Color" = "backgroundColor"
  ? `${First}${Capitalize<KebabToCamel<Rest>>}`
  // : S: 하이픈이 없으면 원본 그대로 반환
  : S;

// type C: 'background-color' 변환 과정
// 1차: "background" + Capitalize(KebabToCamel("color"))
// 2차: KebabToCamel("color") = "color" (하이픈 없음)
// 3차: Capitalize("color") = "Color"
// 결과: "backgroundColor"
type C = KebabToCamel<'background-color'>; // "backgroundColor"

type D = KebabToCamel<'font-size'>; // "fontSize"

// ===== 3. 문자열 분할 =====

// type Split: 문자열을 구분자로 분할하는 타입
// <S extends string, D extends string>: S는 분할할 문자열, D는 구분자
type Split
  S extends string,
  D extends string
// > = S extends `${infer First}${D}${infer Rest}`: S가 "앞부분 + 구분자 + 뒷부분" 패턴인지
//   infer First: 구분자 앞의 문자열
//   ${D}: 구분자 자체
//   infer Rest: 구분자 뒤의 문자열
> = S extends `${infer First}${D}${infer Rest}`
  // ? [First, ...Split<Rest, D>]: 매칭되면
  //   [First, ...]: 배열의 첫 요소로 First 추가
  //   Split<Rest, D>: Rest를 재귀적으로 분할
  //   ...: 재귀 결과를 펼쳐서 배열에 추가 (스프레드)
  ? [First, ...Split<Rest, D>]
  // : S extends D: 구분자가 없으면, S 자체가 구분자인지 확인
  : S extends D
  // ? []: S가 구분자면 빈 배열 (예: "." 분할 시 마지막 "."는 빈 배열)
  ? []
  // : [S]: 구분자가 아니면 S를 배열로 감싸서 반환
  : [S];

// type E: 'a.b.c'를 '.'로 분할
// 1차: "a" + Split("b.c", ".")
// 2차: "b" + Split("c", ".")
// 3차: "c"는 구분자 없음 → ["c"]
// 결과: ["a", "b", "c"]
type E = Split<'a.b.c', '.'>; // ["a", "b", "c"]

// type F: 'hello'를 ''로 분할 (한 글자씩)
// 1차: "h" + Split("ello", "")
// 2차: "e" + Split("llo", "")
// ...
// 결과: ["h", "e", "l", "l", "o"]
type F = Split<'hello', ''>; // ["h", "e", "l", "l", "o"]

// ===== 4. 문자열 결합 =====

// type Join: 문자열 배열을 구분자로 결합하는 타입
// <T extends string[], D extends string>: T는 문자열 배열, D는 구분자
// = T extends [infer First, ...infer Rest]: T가 "첫 요소 + 나머지" 패턴인지
//   infer First: 첫 번째 요소
//   ...infer Rest: 나머지 요소들 (배열)
type Join<T extends string[], D extends string> = T extends [
  infer First,
  ...infer Rest
]
  // ? `${First}${...}`: 매칭되면
  //   ${First}: 첫 번째 요소 추가
  //   Rest extends string[]: Rest가 문자열 배열인지 확인 (타입 가드)
  //     ? `${D}${Join<Rest, D>}`: 문자열 배열이면
  //       ${D}: 구분자 추가
  //       ${Join<Rest, D>}: 나머지를 재귀적으로 결합
  //     : '': 문자열 배열이 아니면 빈 문자열 (마지막 요소)
  ? `${First}${Rest extends string[] ? `${D}${Join<Rest, D>}` : ''}`
  // : '': 배열이 비어있으면 빈 문자열 반환
  : '';

// type G: ['a', 'b', 'c']를 '.'로 결합
// 1차: "a" + "." + Join(["b", "c"], ".")
// 2차: "b" + "." + Join(["c"], ".")
// 3차: "c" + "" (Rest는 빈 배열)
// 결과: "a.b.c"
type G = Join<['a', 'b', 'c'], '.'>; // "a.b.c"

type H = Join<['hello', 'world'], ' '>; // "hello world"