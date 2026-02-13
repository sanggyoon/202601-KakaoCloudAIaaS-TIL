//TODO: 다음 인터페이스들을 정의하세요

// 1. User: id(number), name(string), email(string), age(optional number)
// 2. Post: id(number), title(string), content(string), author(User),
//    createdAt(Date), tags(string array)
// 3. Comment: id(number), content(string), author(User), post(Post)
// 4. API Response: success(boolean), data(generic), error(optional string)

interface User {
  id: number;
  name: string;
  email: string;
  age?: number;
}

interface Post {
  id: number;
  title: string;
  content: string;
  author: User;
  createdAt: Date;
  tags: string[];
}

interface Comment {
  id: number;
  content: string;
  author: User;
  post: Post;
}

interface ApiResponse<T> {
  success: boolean;
  data: T;
  error?: string;
}

// 테스트
const user: User = {
  id: 1,
  name: 'Kim',
  email: 'kim@test.com',
};

const post: Post = {
  id: 1,
  title: 'Hello',
  content: 'World',
  author: user,
  createdAt: new Date(),
  tags: ['typescript', 'tutorial'],
};

const response: ApiResponse<User[]> = {
  success: true,
  data: [user],
};
