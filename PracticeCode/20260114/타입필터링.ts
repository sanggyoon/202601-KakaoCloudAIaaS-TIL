// 1. 특정 타입의 키만 추출
type KeysOfType<T, V> = {
  [K in keyof T]: T[K] extends V ? K : never;
}[keyof T];

// 2. 특정 타입의 속성만 추출
type PickByType<T, V> = {
  [K in KeysOfType<T, V> as K]: T[K];
};

// 3. 특정 타입의 속성 제외
type OmitByType<T, V> = {
  [K in Exclude<keyof T, KeysOfType<T, V>>]: T[K];
};

// 4. 함수 속성만 추출
type FunctionKeys<T> = KeysOfType<T, Function>;
type PickFunctions<T> = PickByType<T, Function>;
// 테스트
interface Mixed {
  id: number;
  name: string;
  active: boolean;
  tags: string[];
  greet: () => void;
  calculate: (x: number) => number;
}

type StringKeys = KeysOfType<Mixed, string>; // "name"
type StringProps = PickByType<Mixed, string>; // { name: string }
type WithoutFunctions = OmitByType<Mixed, Function>;
// { id: number; name: string; active: boolean; tags: string[] }
