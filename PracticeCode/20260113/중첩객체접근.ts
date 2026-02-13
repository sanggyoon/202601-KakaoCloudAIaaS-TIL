/**
 * 중첩된 객체의 모든 가능한 점 표기 경로를 문자열 타입으로 생성
 *
 * 예시:
 * type Example = { a: { b: string, c: number } }
 * NestedKeyOf<Example> = "a" | "a.b" | "a.c"
 */
type NestedKeyOf<T> = T extends object // T가 객체 타입인 경우에만 동작
  ? {
      [K in keyof T & string]:  // T의 모든 키를 순회 (문자열 키만)
        | K // 현재 키 자체 ("a")
        | (T[K] extends object // 현재 키의 값이 객체라면
            ? `${K}.${NestedKeyOf<T[K]>}` // 재귀적으로 하위 경로 생성 ("a.b", "a.b.c")
            : never); // 객체가 아니면 더 이상 경로 생성 안함
    }[keyof T & string] // 유니온 타입으로 결합
  : never; // T가 객체가 아니면 never 반환

/**
 * 점 표기 경로 문자열을 실제 값의 타입으로 변환
 *
 * 예시:
 * PathValue<{ a: { b: string } }, "a.b"> = string
 *
 * 동작 방식:
 * "a.b.c" → T["a"]["b"]["c"] 타입으로 변환
 */
type PathValue<T, P extends string> = P extends `${infer K}.${infer Rest}` // 경로를 첫 번째 키(K)와 나머지(Rest)로 분리
  ? K extends keyof T // K가 T의 유효한 키인지 확인
    ? PathValue<T[K], Rest> // 재귀적으로 나머지 경로 탐색
    : never // 유효하지 않은 키면 never
  : P extends keyof T // 더 이상 점이 없는 경우 (마지막 키)
  ? T[P] // 해당 키의 타입 반환
  : never; // 유효하지 않은 키면 never

// 중첩 객체에서 점 표기법으로 값을 안전하게 가져오는 함수

// @param obj - 값을 가져올 대상 객체
// @param path - 점으로 구분된 경로 문자열 (예: "user.profile.name")
// @returns 경로에 해당하는 값 (타입 안전성 보장)

function getNestedValue<T, K extends NestedKeyOf<T>>(
  obj: T,
  path: K // K는 T의 유효한 경로만 허용
): PathValue<T, K> {
  // 반환 타입은 경로에 해당하는 실제 값의 타입
  // 경로를 점(.)으로 분리하여 배열로 변환
  const keys = path.split('.');

  // 결과를 저장할 변수 (초기값은 최상위 객체)
  let result: any = obj;

  // 각 키를 순회하면서 단계적으로 깊이 들어감
  for (const key of keys) {
    result = result[key]; // result.user → result.user.profile → ...
  }

  // 최종 값 반환
  return result;
}
