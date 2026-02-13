// API 함수들
async function fetchUser(id: number) {
  return { id, name: 'User', email: 'user@test.com' };
}

async function fetchPosts(userId: number, page: number = 1) {
  return [{ id: 1, title: 'Post 1', userId }];
}

async function createPost(userId: number, title: string, content: string) {
  return { id: Date.now(), userId, title, content };
}

// ===== 1. 각 함수의 반환 타입 추출 =====

// ReturnType<typeof 함수>: 함수의 반환 타입 추출
// async 함수는 Promise를 반환하므로 Awaited로 Promise 벗기기
type User = Awaited<ReturnType<typeof fetchUser>>;
// { id: number; name: string; email: string }

type Posts = Awaited<ReturnType<typeof fetchPosts>>;
// { id: number; title: string; userId: number }[]
// 배열이므로 Posts로 명명

type NewPost = Awaited<ReturnType<typeof createPost>>;
// { id: number; userId: number; title: string; content: string }

// ===== 2. 각 함수의 매개변수 타입 추출 =====

// Parameters<typeof 함수>: 함수의 매개변수를 튜플로 추출
type FetchUserParams = Parameters<typeof fetchUser>;
// [id: number]

type FetchPostsParams = Parameters<typeof fetchPosts>;
// [userId: number, page?: number]

type CreatePostParams = Parameters<typeof createPost>;
// [userId: number, title: string, content: string]

// ===== 3. 로깅 래퍼 함수 구현 =====

function withLogging<T extends (...args: any[]) => Promise<any>>(
  fn: T,
  name: string
): (...args: Parameters<T>) => ReturnType<T> {
  return (async (...args: Parameters<T>) => {
    console.log(`[${name}] 시작, 인자:`, args);
    const result = await fn(...args);
    console.log(`[${name}] 완료, 결과:`, result);
    return result;
  }) as any;
}

// ===== 4. 재시도 래퍼 함수 구현 =====

function withRetry<T extends (...args: any[]) => Promise<any>>(
  fn: T,
  maxRetries: number
): (...args: Parameters<T>) => ReturnType<T> {
  return (async (...args: Parameters<T>) => {
    for (let attempt = 0; attempt <= maxRetries; attempt++) {
      try {
        return await fn(...args);
      } catch (error) {
        if (attempt === maxRetries) throw error;
        console.log(`재시도 ${attempt + 1}/${maxRetries}`);
      }
    }
  }) as any;
}
