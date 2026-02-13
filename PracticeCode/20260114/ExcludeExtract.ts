type ApiEvent =
  | { type: 'request'; url: string; method: string }
  | { type: 'response'; status: number; data: unknown }
  | { type: 'error'; message: string; code: number }
  | { type: 'timeout'; duration: number }
  | { type: 'retry'; attempt: number; maxAttempts: number };

// 1. 성공 이벤트만 추출 (request, response)
type SuccessEvent = Extract<ApiEvent, { type: 'request' | 'response' }>;

// 2. 실패 이벤트만 추출 (error, timeout)
type FailureEvent = Exclude<ApiEvent, SuccessEvent>;

// 3. 특정 타입의 이벤트 추출 함수
function filterEvents<T extends ApiEvent['type']>(
  events: ApiEvent[],
  type: T
): Extract<ApiEvent, { type: T }>[] {
  // 구현하세요
  return events.filter((event) => event.type === type) as Extract<
    ApiEvent,
    { type: T }
  >[];
}

// 4. 이벤트 핸들러 타입
type EventHandler<T extends ApiEvent['type']> = (
  event: Extract<ApiEvent, { type: T }>
) => void;

// 이벤트 디스패처 구현
class EventDispatcher {
  private handlers = new Map<string, Function[]>();

  on<T extends ApiEvent['type']>(type: T, handler: EventHandler<T>): void {
    // 구현하세요
    if (!this.handlers.has(type)) {
      this.handlers.set(type, []);
    }
    this.handlers.get(type)!.push(handler);
  }

  dispatch(event: ApiEvent): void {
    // 구현하세요
    const handlers = this.handlers.get(event.type);
    if (handlers) {
      handlers.forEach((handler) => handler(event));
    }
  }
}
