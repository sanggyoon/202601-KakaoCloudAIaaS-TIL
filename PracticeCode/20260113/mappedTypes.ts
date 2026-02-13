type Nullable<T> = { [K in keyof T]: T[K] | null };

type User0 = { id: number; name: string };
type UserOrNull = Nullable<User0>;
