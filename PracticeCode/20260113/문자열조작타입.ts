// 문자열을 대문자로
type Uppercase<S extends string> = Uppercase<S>;

// 첫 글자만 대문자
type Capitalize<S extends string> = Capitalize<S>;

// camelCase를 snake_case로
type CamelToSnake<S extends string> = S extends `${infer First}${infer Rest}`
  ? `${First}${Rest extends `${infer UppercaseChar}${infer Rest}`
      ? UppercaseChar extends Uppercase<UppercaseChar>
        ? `_${Lowercase<UppercaseChar>}${Rest}`
        : `${UppercaseChar}${Rest}`
      : Rest}`
  : S;

// 점 표기법 경로를 튜플로
type PathToTuple<S extends string> = S extends `${infer First}.${infer Rest}`
  ? [First, ...PathToTuple<Rest>]
  : [S];

// 테스트
type A = Capitalize<'hello'>; // "Hello"
type B = CamelToSnake<'getUserName'>; // "get_user_name"
type C = PathToTuple<'a.b.c'>; // ["a", "b", "c"]
