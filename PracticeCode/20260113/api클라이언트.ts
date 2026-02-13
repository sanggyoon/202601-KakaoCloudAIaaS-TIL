// ===============================
// User 도메인 모델
// ===============================

// 사용자 한 명의 데이터 구조를 정의하는 인터페이스
interface User {
  id: number; // 사용자 고유 ID
  name: string; // 사용자 이름
  email: string; // 사용자 이메일
}

// ===============================
// Post 도메인 모델
// ===============================

// 게시글 한 개의 데이터 구조
interface Post {
  id: number; // 게시글 ID
  userId: number; // 작성자(User)의 ID
  title: string; // 게시글 제목
  body: string; // 게시글 내용
}

// ===============================
// API 엔드포인트 타입 정의
// ===============================

// API 경로별로
// - 허용되는 HTTP 메서드
// - 각 메서드의 요청/응답 타입
// 을 명확하게 선언한 "API 명세서"
interface ApiEndpoints {
  '/users': {
    GET: User[]; // GET /users → User 배열 반환
    POST: Omit<User, 'id'>; // POST /users → id 없이 사용자 생성
  };

  '/users/:id': {
    GET: User; // GET /users/:id → User 하나
    PUT: Partial<User>; // PUT /users/:id → 일부 수정
    DELETE: void; // DELETE /users/:id → 반환값 없음
  };

  '/posts': {
    GET: Post[]; // GET /posts → Post 배열
    POST: Omit<Post, 'id'>; // POST /posts → id 없이 생성
  };

  '/posts/:id': {
    GET: Post; // GET /posts/:id → Post 하나
    PUT: Partial<Post>; // PUT /posts/:id → 일부 수정
    DELETE: void; // DELETE /posts/:id → 반환값 없음
  };
}

// ===============================
// PathParams 타입
// ===============================

// URL 경로 문자열에서 ":id" 같은 동적 파라미터를 추출하는 타입
type PathParams<Path extends string> =
  // Path가 "...:param" 형태를 만족하는지 검사
  Path extends `${string}:${infer Param}`
    ? // 만족하면 param 이름을 키로 갖는 객체 타입 생성
      { [K in Param]: number }
    : // 없으면 params 자체가 필요 없으므로 undefined
      undefined;

// ===============================
// API Client 생성 함수
// ===============================

// Endpoints는 ApiEndpoints 같은 구조를 강제
function createApiClient<
  Endpoints extends Record<string, any> // 엔드포인트 맵 제약
>(baseUrl: string) {
  // API 기본 URL

  // API 메서드 객체 반환
  return {
    // ===============================
    // GET 메서드
    // ===============================
    get<Path extends keyof Endpoints>(
      // path는 Endpoints에 정의된 경로만 허용
      path: Path,

      // path에 ":id"가 있을 경우에만 params 필요
      params?: PathParams<Path & string>
    ): Promise<Endpoints[Path]['GET']> {
      // 실제 HTTP 구현은 생략
      // 타입 안전성만 검증하기 위해 any 캐스팅
      return Promise.resolve(null as any);
    },

    // ===============================
    // POST 메서드
    // ===============================
    post<Path extends keyof Endpoints>(
      // 엔드포인트 경로
      path: Path,

      // POST 요청 바디 타입은 엔드포인트 정의를 따름
      body: Endpoints[Path]['POST']
    ): Promise<void> {
      // 요구사항: 반환값 없음
      return Promise.resolve();
    },

    // ===============================
    // PUT 메서드
    // ===============================
    put<Path extends keyof Endpoints>(
      // 엔드포인트 경로
      path: Path,

      // PUT 요청 바디 타입
      body: Endpoints[Path]['PUT']
    ): Promise<void> {
      return Promise.resolve();
    },

    // ===============================
    // DELETE 메서드
    // ===============================
    delete<Path extends keyof Endpoints>(
      // 엔드포인트 경로
      path: Path,

      // ":id"가 있는 경우만 params 사용
      params?: PathParams<Path & string>
    ): Promise<void> {
      return Promise.resolve();
    },
  };
}

// ===============================
// 사용 예 (타입 추론 확인용)
// ===============================

// ApiEndpoints를 기반으로 API 클라이언트 생성
const api = createApiClient<ApiEndpoints>('https://api.example.com');

// GET /users
// 반환 타입: User[]
const users = await api.get('/users');

// GET /users/:id
// params 타입 자동 추론: { id: number }
// 반환 타입: User
const user = await api.get('/users/:id', { id: 1 });

// POST /users
// body 타입: Omit<User, 'id'>
// 반환 타입: void
const newUser = await api.post('/users', {
  name: 'Kim',
  email: 'kim@test.com',
});

// DELETE /users/:id
// params 타입 강제
// 반환 타입: void
await api.delete('/users/:id', { id: 1 });
