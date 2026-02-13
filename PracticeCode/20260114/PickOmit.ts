interface User {
  id: number;
  email: string;
  password: string;
  name: string;
  role: 'admin' | 'user' | 'guest';
  createdAt: Date;
  updatedAt: Date;
  lastLoginAt: Date | null;
}

// 1. 로그인 응답 타입 (id, email, name, role만)
type LoginResponse = Pick<User, 'id' | 'email' | 'name' | 'role'>;

// 2. 사용자 목록 아이템 타입 (password, lastLoginAt 제외)
type UserListItem = Omit<User, 'password' | 'lastLoginAt'>;

// 3. 회원가입 요청 타입 (id, createdAt, updatedAt, lastLoginAt 제외)
type SignupRequest = Omit<
  User,
  'id' | 'createdAt' | 'updatedAt' | 'lastLoginAt'
>;

// 4. 프로필 수정 요청 타입 (name만 수정 가능)
type UpdateProfileRequest = Pick<User, 'name'>;

// 5. 변환 함수들 구현
function toLoginResponse(user: User): LoginResponse {
  // 구현하세요
  return {
    id: user.id,
    email: user.email,
    name: user.name,
    role: user.role,
  };
}

function toUserListItem(user: User): UserListItem {
  // 구현하세요
  return {
    id: user.id,
    email: user.email,
    name: user.name,
    role: user.role,
    createdAt: user.createdAt,
    updatedAt: user.updatedAt,
  };
}
