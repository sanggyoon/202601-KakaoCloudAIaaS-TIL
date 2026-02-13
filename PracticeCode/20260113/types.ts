type User = {
  name: string;
  age: number;
  email?: string;
};

// 객체 외 타입 선언
type ID = number | string;
type Point = [number, number];
type Callback = (value: string) => void;
