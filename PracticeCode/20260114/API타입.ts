// 타입 정의 추가
interface User {
  id: number;
  name: string;
  email: string;
}

interface CreateUserDto {
  name: string;
  email: string;
}

interface UpdateUserDto {
  name?: string;
  email?: string;
}

// API 정의 수정 (모든 필드 선택적으로)
interface ApiDefinition {
  request?: unknown;
  response?: unknown;
  params?: unknown;
  query?: unknown;
}

// API 정의
interface ApiDefinition {
  request?: unknown;
  response?: unknown;
  params?: unknown;
  query?: unknown;
}

interface UserApi {
  'GET /users': {
    response: User[];
    query: { page?: number; limit?: number };
  };
  'GET /users/:id': {
    response: User;
    params: { id: number };
  };
  'POST /users': {
    request: CreateUserDto;
    response: User;
  };
  'PUT /users/:id': {
    request: UpdateUserDto;
    response: User;
    params: { id: number };
  };
  'DELETE /users/:id': {
    response: void;
    params: { id: number };
  };
}

// 1. API 경로 추출
type ApiPath<T> = keyof T;

// 2. 특정 경로의 요청 타입
type RequestOf<T, P extends keyof T> = T[P] extends { request: infer Req }
  ? Req
  : never;

// 3. 특정 경로의 응답 타입
type ResponseOf<T, P extends keyof T> = T[P] extends { response: infer Res }
  ? Res
  : never;

// 4. API 클라이언트 구현
class ApiClient<T extends Record<string, ApiDefinition>> {
  async request<P extends keyof T>(
    path: P,
    options?: {
      params?: T[P] extends { params: infer Params } ? Params : never;
      query?: T[P] extends { query: infer Query } ? Query : never;
      body?: T[P] extends { request: infer Req } ? Req : never;
    }
  ): Promise<T[P] extends { response: infer Res } ? Res : never> {
    // 구현하세요
    return Promise.resolve(undefined as any);
  }
}

// 사용
const api = new ApiClient<UserApi>();
// const users = await api.request("GET /users", { query: { page: 1 } });
