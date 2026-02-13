// 기본 인터페이스
interface IQueue<T> {
  enqueue(item: T): void;
  dequeue(): T | undefined;
  peek(): T | undefined;
  isEmpty(): boolean;
}

interface IStack<T> {
  push(item: T): void;
  pop(): T | undefined;
  peek(): T | undefined;
  isEmpty(): boolean;
}

// 우선순위 큐 구현 - 비교 함수 사용
class PriorityQueue<T> implements IQueue<T> {
  constructor(private compareFn: (a: T, b: T) => number) {}

  // 구현하세요
  // 높은 우선순위가 먼저 나오도록
  private items: T[] = [];

  enqueue(item: T): void {
    this.items.push(item);
    this.items.sort(this.compareFn);
  }

  dequeue(item?: T): T | undefined {
    return this.items.shift();
  }

  peek(): T | undefined {
    return this.items[0];
  }

  isEmpty(): boolean {
    return this.items.length === 0;
  }
}

// 테스트
const pq = new PriorityQueue<{ task: string; priority: number }>(
  (a, b) => b.priority - a.priority
);
pq.enqueue({ task: 'low', priority: 1 });
pq.enqueue({ task: 'high', priority: 10 });
pq.enqueue({ task: 'medium', priority: 5 });

console.log(pq.dequeue()); // { task: "high", priority: 10 }
console.log(pq.dequeue()); // { task: "medium", priority: 5 }
