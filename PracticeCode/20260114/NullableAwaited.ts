interface ApiResponse<T> {
  data: T | null;
  error: string | null;
  timestamp: Date;
}

// ===== 1. 응답에서 데이터 안전하게 추출 =====

// function extractData: 함수 이름
// <T>: 제네릭 타입 매개변수
// (response: ApiResponse<T>): 매개변수
// : NonNullable<T> | never: 반환 타입 (null 제거된 T 또는 에러)
function extractData<T>(response: ApiResponse<T>): NonNullable<T> | never {
  // if (response.data === null): data가 null인지 확인
  if (response.data === null) {
    // throw new Error: 에러 던지기 (함수 중단)
    // response.error || 'No data': error가 있으면 그것을, 없으면 기본 메시지
    throw new Error(response.error || 'No data');
  }

  // return response.data as NonNullable<T>: null이 아님을 보장하고 반환
  // as NonNullable<T>: 타입 단언 (위에서 null 체크했으므로 안전)
  return response.data as NonNullable<T>;
}

// ===== 2. 여러 Promise 결과를 안전하게 처리 =====

// type PromiseResults: 유틸리티 타입 정의
// <T extends Promise<any>[]>: T는 Promise 배열이어야 함
// = { [K in keyof T]: Awaited<T[K]> }: 매핑된 타입
type PromiseResults<T extends Promise<any>[]> = {
  // [K in keyof T]: T의 모든 인덱스(키)를 순회
  // : Awaited<T[K]>: 각 Promise의 결과 타입으로 변환
  //   - T[K]: K번째 Promise
  //   - Awaited<>: Promise를 벗겨서 실제 값의 타입 추출
  [K in keyof T]: Awaited<T[K]>;
};

// async function safeAll: 비동기 함수
// <T extends Promise<any>[]>: T는 Promise 배열
// (...promises: T): 나머지 매개변수로 여러 Promise를 받음
// : Promise<PromiseResults<T>>: 모든 Promise 결과의 튜플 반환
async function safeAll<T extends Promise<any>[]>(
  ...promises: T
): Promise<PromiseResults<T>> {
  // return await Promise.all(promises): 모든 Promise를 병렬 실행하고 대기
  // Promise.all(...): 모든 Promise가 완료될 때까지 대기, 결과를 배열로 반환
  // as PromiseResults<T>: 정확한 튜플 타입으로 단언
  return (await Promise.all(promises)) as PromiseResults<T>;
}

// ===== 3. 옵셔널 체이닝 결과 타입 처리 =====

// interface DeepObject: 깊게 중첩된 객체 구조
interface DeepObject {
  // level1?: 선택적 프로퍼티 (undefined일 수 있음)
  level1?: {
    // level2?: 선택적 프로퍼티
    level2?: {
      // level3?: 선택적 프로퍼티
      level3?: {
        // value: 필수 프로퍼티
        value: string;
      };
    };
  };
}

// function getDeepValue: 안전하게 깊은 값 추출
// (obj: DeepObject): 매개변수
// : NonNullable<string> | undefined: 반환 타입 (string 또는 undefined)
function getDeepValue(obj: DeepObject): NonNullable<string> | undefined {
  // return obj.level1?.level2?.level3?.value: 옵셔널 체이닝으로 안전하게 접근
  // ?.: 앞의 값이 null/undefined면 undefined 반환, 아니면 다음 속성 접근
  // 중간에 하나라도 undefined면 전체 결과가 undefined
  return obj.level1?.level2?.level3?.value;
}
