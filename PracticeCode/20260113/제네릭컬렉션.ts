interface Collection<T> {
  add(item: T): void;
  remove(item: T): boolean;
  contains(item: T): boolean;
  size(): number;
  toArray(): T[];
}

// Set 기반 컬렉션 구현
class UniqueCollection<T> implements Collection<T> {
  // 구현하세요
  private items: Set<T>;

  constructor() {
    this.items = new Set<T>();
  }

  add(item: T): void {
    this.items.add(item);
  }

  remove(item: T): boolean {
    return this.items.delete(item);
  }

  contains(item: T): boolean {
    return this.items.has(item);
  }

  size(): number {
    return this.items.size;
  }

  toArray(): T[] {
    return Array.from(this.items);
  }
}

// 테스트
const collection = new UniqueCollection<number>();
collection.add(1);
collection.add(2);
collection.add(1); // 중복 무시
console.log(collection.size()); // 2
console.log(collection.contains(1)); // true
console.log(collection.toArray()); // [1, 2]
