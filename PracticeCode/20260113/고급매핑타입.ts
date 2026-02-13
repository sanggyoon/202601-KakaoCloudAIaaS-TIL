// 특정 키만 선택
type MyPick<T, K extends keyof T> = { [P in K]: T[P] };

// 특정 키 제외
type MyOmit<T, K extends keyof T> = {
  [P in keyof T as P extends K ? never : P]: T[P];
};

// 속성 이름에 접두사 추가
type Prefixed<T, P extends string> = {
  [K in keyof T as `${P}${K & string}`]: T[K];
};

// Getter 함수 타입 생성
type Getters<T> = {
  [K in keyof T as `get${Capitalize<K & string>}`]: () => T[K];
};

// Setter 함수 타입 생성
type Setters<T> = {
  [K in keyof T as `set${Capitalize<K & string>}`]: (value: T[K]) => void;
};

// 테스트
type User = { name: string; age: number };

type NameOnly = MyPick<User, 'name'>; // { name: string }
type WithoutAge = MyOmit<User, 'age'>; // { name: string }

type PrefixedUser = Prefixed<User, 'user_'>;
// { user_name: string; user_age: number }

type UserGetters = Getters<User>;
// { getName: () => string; getAge: () => number }

type UserSetters = Setters<User>;
// { setName: (value: string) => void; setAge: (value: number) => void }
