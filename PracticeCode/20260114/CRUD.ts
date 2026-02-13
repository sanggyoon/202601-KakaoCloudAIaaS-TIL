interface Entity {
  id: number;
  createdAt: Date;
  updatedAt: Date;
}

interface User extends Entity {
  email: string;
  password: string;
  name: string;
  role: 'admin' | 'user';
}

// 1. 생성 DTO (Entity 필드 제외)
type CreateDto<T extends Entity> = Omit<T, keyof Entity>;

// 2. 업데이트 DTO (id, createdAt 제외, 나머지 옵셔널)
type UpdateDto<T extends Entity> = Partial<Omit<T, keyof Entity>>;

// 3. 조회 응답 (password 같은 민감 필드 제외)
type ViewDto<T, K extends keyof T> = Omit<T, K>;

// 4. 목록 응답 (일부 필드만)
type ListItemDto<T, K extends keyof T> = Pick<T, K>;

// User에 적용
type CreateUserDto = CreateDto<User>;
type UpdateUserDto = UpdateDto<User>;
type UserView = ViewDto<User, 'password'>;
type UserListItem = ListItemDto<User, 'id' | 'name' | 'email'>;
