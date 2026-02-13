type HttpMethod = 'GET' | 'POST' | 'PUT' | 'DELETE' | 'PATCH';
type StatusCode = 200 | 201 | 400 | 401 | 403 | 404 | 500;

// 1. 각 HTTP 메서드별 허용되는 상태 코드 매핑
type AllowedStatusCodes = Record<HttpMethod, StatusCode[]>;

// 구현하세요
const allowedStatusCodes: AllowedStatusCodes = {
  // ...
  GET: [200, 400, 401, 403, 404, 500],
  POST: [201, 400, 401, 403, 500],
  PUT: [200, 400, 401, 403, 404, 500],
  DELETE: [200, 400, 401, 403, 404, 500],
  PATCH: [200, 400, 401, 403, 404, 500],
};

// 2. 상태 코드별 메시지 매핑
type StatusMessages = Record<StatusCode, string>;

const statusMessages: StatusMessages = {
  // ...
  200: 'OK',
  201: 'Created',
  400: 'Bad Request',
  401: 'Unauthorized',
  403: 'Forbidden',
  404: 'Not Found',
  500: 'Internal Server Error',
};

// 3. 캐시 저장소 타입 (문자열 키, 제네릭 값)
type Cache<T> = Record<string, T>;

// 캐시 매니저 구현
class CacheManager<T> {
  private cache: Cache<T> = {};

  set(key: string, value: T): void {
    // 구현하세요
    this.cache[key] = value;
  }

  get(key: string): T | undefined {
    // 구현하세요
    return this.cache[key];
  }

  has(key: string): boolean {
    // 구현하세요
    return key in this.cache;
  }

  delete(key: string): boolean {
    // 구현하세요
    if (key in this.cache) {
      delete this.cache[key];
      return true;
    }
    return false;
  }

  clear(): void {
    // 구현하세요
    this.cache = {};
  }
}
