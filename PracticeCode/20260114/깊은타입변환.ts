// 1. DeepPartial 구현
type DeepPartial<T> = {
  [K in keyof T]?: DeepPartial<T[K]>;
};

// 2. DeepReadonly 구현
type DeepReadonly<T> = {
  readonly [K in keyof T]: DeepReadonly<T[K]>;
};

// 3. DeepRequired 구현
type DeepRequired<T> = {
  [K in keyof T]-?: DeepRequired<T[K]>;
};

// 4. DeepNonNullable 구현
type DeepNonNullable<T> = {
  [K in keyof T]: NonNullable<T[K]>;
};

// 테스트
interface NestedConfig {
  server?: {
    host?: string;
    port?: number;
    ssl?: {
      enabled?: boolean;
      cert?: string | null;
    };
  };
  database?: {
    url?: string | null;
    pool?: {
      min?: number;
      max?: number;
    };
  };
}

type FullConfig = DeepRequired<DeepNonNullable<NestedConfig>>;
// 모든 속성이 필수이고 null이 아님
