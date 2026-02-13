//TODO: 다음 클래스들을 구현하세요

// 1. Stack<T>: push, pop, peek, isEmpty, size
// 2. Queue<T>: enqueue, dequeue, front, isEmpty, size
// 3. LinkedList<T>: append, prepend, delete, find, toArray
class Stack<T> {
  private items: T[] = [];
  push(items: T): void {
    this.items.push(items);
  }
  pop(): T | undefined {
    return this.items.pop();
  }
  peek(): T | undefined {
    return this.items[this.items.length - 1];
  }
  isEmpty(): boolean {
    return this.items.length === 0;
  }
  size(): number {
    return this.items.length;
  }
}

class Queue<T> {
  private items: T[] = [];
  enqueue(item: T): void {
    this.items.push(item);
  }
  dequeue(): T | undefined {
    return this.items.shift();
  }
  front(): T | undefined {
    return this.items[0];
  }
  isEmpty(): boolean {
    return this.items.length === 0;
  }
  size(): number {
    return this.items.length;
  }
}

class ListNode<T> {
  constructor(public value: T, public next: ListNode<T> | null = null) {}
}
class LinkedList<T> {
  private head: ListNode<T> | null = null;

  append(value: T): void {
    const newNode = new ListNode(value);

    if (!this.head) {
      this.head = newNode;
      return;
    }

    let current = this.head;
    while (current.next) {
      current = current.next;
    }
    current.next = newNode;
  }

  prepend(value: T): void {
    this.head = new ListNode(value, this.head);
  }

  delete(value: T): void {
    if (!this.head) return;

    if (this.head.value === value) {
      this.head = this.head.next;
      return;
    }

    let current = this.head;
    while (current.next) {
      if (current.next.value === value) {
        current.next = current.next.next;
        return;
      }
      current = current.next;
    }
  }

  find(value: T): ListNode<T> | null {
    let current = this.head;
    while (current) {
      if (current.value === value) return current;
      current = current.next;
    }
    return null;
  }

  toArray(): T[] {
    const result: T[] = [];
    let current = this.head;
    while (current) {
      result.push(current.value);
      current = current.next;
    }
    return result;
  }
}

// 테스트
const stack = new Stack<number>();
stack.push(1);
stack.push(2);
console.log(stack.pop()); // 2
console.log(stack.peek()); // 1
console.log(stack.size()); // 1

const queue = new Queue<string>();
queue.enqueue('a');
queue.enqueue('b');
console.log(queue.dequeue()); // "a"
console.log(queue.front()); // "b"

const list = new LinkedList<number>();
list.append(1);
list.append(2);
list.prepend(0);
console.log(list.toArray()); // [0, 1, 2]
list.delete(1);
console.log(list.toArray()); // [0, 2]
