type EventMap = {
  userLogin: { userId: string; timestamp: Date };
  userLogout: { userId: string };
  pageView: { path: string; referrer?: string };
  error: { message: string; code: number };
};

class TypedEventEmitter<T extends Record<string, any>> {
  // on: 이벤트 리스너 등록
  // off: 이벤트 리스너 제거
  // emit: 이벤트 발생
  // once: 한 번만 실행되는 리스너
  // 구현하세요
  private listeners: { [K in keyof T]?: Array<(data: T[K]) => void> } = {};

  on<K extends keyof T>(event: K, listener: (data: T[K]) => void): void {
    if (!this.listeners[event]) {
      this.listeners[event] = [];
    }
    this.listeners[event]!.push(listener);
  }

  off<K extends keyof T>(event: K, listener: (data: T[K]) => void): void {
    if (!this.listeners[event]) return;
    this.listeners[event] = this.listeners[event]!.filter(
      (l) => l !== listener
    );
  }

  emit<K extends keyof T>(event: K, data: T[K]): void {
    if (!this.listeners[event]) return;
    for (const listener of this.listeners[event]!) {
      listener(data);
    }
  }

  once<K extends keyof T>(event: K, listener: (data: T[K]) => void): void {
    const onceListener = (data: T[K]) => {
      listener(data);
      this.off(event, onceListener);
    };
    this.on(event, onceListener);
  }
}

// 테스트
const emitter = new TypedEventEmitter<EventMap>();

emitter.on('userLogin', (data) => {
  console.log(data.userId); // 타입 추론됨
});

emitter.emit('userLogin', {
  userId: '123',
  timestamp: new Date(),
});

// 타입 에러:
// emitter.emit("userLogin", { userId: 123 });
// emitter.emit("unknownEvent", {});
