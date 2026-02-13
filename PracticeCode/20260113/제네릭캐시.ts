interface Cache<K, V> {
  get(key: K): V | undefined;
  set(key: K, value: V): void;
  has(key: K): boolean;
  delete(key: K): boolean;
  clear(): void;
}

// TTL(Time To Live) 지원 캐시 구현
class TTLCache<K, V> implements Cache<K, V> {
  private cache = new Map<K, { value: V; expiresAt: number }>();

  constructor(private defaultTTL: number = 60000) {}

  // 구현하세요
  // set 시 TTL 지정 가능하도록
  set(key: K, value: V): void {
    const expiresAt = Date.now() + this.defaultTTL;
    this.cache.set(key, { value, expiresAt });
  }

  get(key: K): V | undefined {
    const entry = this.cache.get(key);
    if (!entry) return undefined;
    if (Date.now() > entry.expiresAt) {
      this.cache.delete(key);
      return undefined;
    }
    return entry.value;
  }

  has(key: K): boolean {
    const entry = this.cache.get(key);
    if (!entry) return false;
    if (Date.now() > entry.expiresAt) {
      this.cache.delete(key);
      return false;
    }
    return true;
  }

  delete(key: K): boolean {
    return this.cache.delete(key);
  }

  clear(): void {
    this.cache.clear();
  }
}

// 테스트
const cache = new TTLCache<string, number>(1000); // 1초 TTL
cache.set('key1', 100);
console.log(cache.get('key1')); // 100

setTimeout(() => {
  console.log(cache.get('key1')); // undefined (만료됨)
}, 1500);
