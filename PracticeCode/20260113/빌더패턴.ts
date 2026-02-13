// 타입 안전 쿼리 빌더 구현
interface QueryBuilder<T> {
  select<K extends keyof T>(...fields: K[]): QueryBuilder<Pick<T, K>>;
  where<K extends keyof T>(field: K, value: T[K]): QueryBuilder<T>;
  orderBy<K extends keyof T>(
    field: K,
    direction: 'asc' | 'desc'
  ): QueryBuilder<T>;
  limit(count: number): QueryBuilder<T>;
  build(): string;
}

function createQueryBuilder<T>(table: string): QueryBuilder<T> {
  // 구현하세요
  const selections: string[] = [];
  const conditions: string[] = [];
  let orderClause = '';
  let limitClause = '';

  return {
    select<K extends keyof T>(...fields: K[]) {
      selections.push(...(fields as string[]));
      return this as QueryBuilder<Pick<T, K>>;
    },
    where<K extends keyof T>(field: K, value: T[K]) {
      conditions.push(`${String(field)} = ${JSON.stringify(value)}`);
      return this;
    },
    orderBy<K extends keyof T>(field: K, direction: 'asc' | 'desc') {
      orderClause = `ORDER BY ${String(field)} ${direction.toUpperCase()}`;
      return this;
    },
    limit(count: number) {
      limitClause = `LIMIT ${count}`;
      return this;
    },
    build() {
      const selectClause = selections.length > 0 ? selections.join(', ') : '*';
      const whereClause =
        conditions.length > 0 ? `WHERE ${conditions.join(' AND ')}` : '';
      return `SELECT ${selectClause} FROM ${table} ${whereClause} ${orderClause} ${limitClause}`.trim();
    },
  };
}

// 테스트
interface User {
  id: number;
  name: string;
  email: string;
  age: number;
}

const query = createQueryBuilder<User>('users')
  .select('id', 'name')
  .where('age', 25)
  .orderBy('name', 'asc')
  .limit(10)
  .build();

// SELECT id, name FROM users WHERE age = 25 ORDER BY name ASC LIMIT 10
