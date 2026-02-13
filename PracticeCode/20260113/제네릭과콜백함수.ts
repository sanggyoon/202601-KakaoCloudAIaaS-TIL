//TODO: 다음 함수들을 타입 안전하게 구현하세요

// 1. 비동기 맵 함수
async function asyncMap<T, U>(
  items: T[],
  callback: (item: T, index: number) => Promise<U>
): Promise<U[]> {
  //TODO
  return Promise.all(items.map(callback));
}

// 2. 이벤트 에미터 타입
interface EventMap {
  click: { x: number; y: number };
  keydown: { key: string; code: string };
  submit: { data: Record<string, string> };
}

class TypedEventEmitter<
  T extends Record<'click' | 'keydown' | 'submit', unknown>
> {
  // TODO do, off, emit 메서드 구현
  private listeners: {
    [K in keyof T]?: Array<(arg: T[K]) => void>;
  } = {};

  on<K extends keyof T>(event: K, listener: (arg: T[K]) => void): void {
    if (!this.listeners[event]) {
      this.listeners[event] = [];
    }
    this.listeners[event]!.push(listener);
  }

  off<K extends keyof T>(event: K, listener: (arg: T[K]) => void): void {
    const handlers = this.listeners[event];
    if (!handlers) return;

    this.listeners[event] = handlers.filter((h) => h !== listener);
  }

  emit<K extends keyof T>(event: K, arg: T[K]): void {
    const handlers = this.listeners[event];
    if (!handlers) return;

    handlers.forEach((handler) => handler(arg));
  }
}

// 테스트
const emitter = new TypedEventEmitter<EventMap>();

emitter.on('click', (event) => {
  console.log(event.x, event.y); // 타입 추론됨
});

emitter.emit('keydown', { key: 'Enter', code: 'Enter' });
emitter.emit('click', { x: 100, y: 200 });
