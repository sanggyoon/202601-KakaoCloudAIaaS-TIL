// 점 표기법으로 중첩 객체 접근 타입 안전하게 구현

// 1. 가능한 모든 경로 추출
type Paths<T, D extends string = '.', Depth extends any[] = []> = Depth['length'] extends 5
  ? never
  : {
      [K in keyof T]: T[K] extends Record<string, any>
        ? `${K & string}${D}${Paths<T[K], D, [...Depth, 1]>}`
        : K & string;
    }[keyof T];

// 2. 경로에 해당하는 값 타입 추출
type PathValue<T, P extends string> = P extends `${infer K}.${infer Rest}`
  ? K extends keyof T
    ? PathValue<T[K], Rest>
    : never
  : P extends keyof T
  ? T[P]
  : never;

// 3. 타입 안전 getter 구현
function get<T, P extends Paths<T>>(obj: T, path: P): PathValue<T, P> {
  // 구현하세요
  const keys = path.split('.');
  let current: any = obj;
  for (const key of keys) {
    if (current === null || current === undefined) {
      return undefined as any;
    }
    current = current[key];
  }
  return current;
}

// 4. 타입 안전 setter 구현
function set<T, P extends Paths<T>>(
  obj: T,
  path: P,
  value: PathValue<T, P>
): T {
  // 구현하세요 (불변성 유지)
  const keys = path.split('.');
  const newObj = { ...obj };
  let current: any = newObj;
  for (let i = 0; i < keys.length - 1; i++) {
    const key = keys[i];
    current[key] = { ...current[key] };
    current = current[key];
  }
  current[keys[keys.length - 1]] = value;
  return newObj;
}

// 테스트
interface Config {
  server: {
    host: string;
    port: number;
  };
  database: {
    connection: {
      url: string;
      pool: {
        min: number;
        max: number;
      };
    };
  };
}

const config: Config = {
  server: { host: 'localhost', port: 3000 },
  database: {
    connection: {
      url: 'mongodb://localhost',
      pool: { min: 5, max: 20 },
    },
  },
};

const host = get(config, 'server.host'); // string
const poolMax = get(config, 'database.connection.pool.max'); // number
