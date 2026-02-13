type EventType = 'click' | 'mouseOver' | 'keyDown' | 'submit';

// 1. 이벤트 핸들러 이름 생성 (onClick, onMouseOver 등)
type EventHandlerName<T extends string> = `on${Capitalize<T>}`;

type ClickHandler = EventHandlerName<'click'>; // "onClick"

// 2. 모든 이벤트에 대한 핸들러 맵 타입
type EventHandlers = {
  [K in EventType as EventHandlerName<K>]: (event: Event) => void;
};

// 3. API 경로를 상수로 변환 (USER_LIST, USER_DETAIL 등)
type ApiPath = '/user/list' | '/user/detail' | '/post/create';

type PathToConstant<T extends string> = T extends `/user/list`
  ? 'USER_LIST'
  : T extends `/user/detail`
  ? 'USER_DETAIL'
  : T extends `/post/create`
  ? 'POST_CREATE'
  : never;

// 4. 구현
const API_PATHS: { [K in ApiPath as PathToConstant<K>]: K } = {
  USER_LIST: '/user/list',
  USER_DETAIL: '/user/detail',
  POST_CREATE: '/post/create',
};
