// Redux 스타일 타입 안전 상태 관리

interface Action<T extends string = string, P = any> {
  type: T;
  payload: P;
}

// 액션 생성자 타입
type ActionCreator<T extends string, P> = (payload: P) => Action<T, P>;

// 리듀서 타입
type Reducer<S, A extends Action> = (state: S, action: A) => S;

// 1. 액션 맵에서 모든 액션 유니온 추출
type ActionsOf<T extends Record<string, ActionCreator<string, any>>> =
  ReturnType<T[keyof T]>;

// 2. 액션 타입 문자열 추출
type ActionTypes<T extends Record<string, ActionCreator<string, any>>> =
  ReturnType<T[keyof T]>['type'];
// 3. 스토어 구현
function createStore<S, A extends Record<string, ActionCreator<string, any>>>(
  reducer: Reducer<S, ActionsOf<A>>,
  initialState: S,
  actions: A
): {
  getState: () => S;
  dispatch: (action: ActionsOf<A>) => void;
  subscribe: (listener: (state: S) => void) => () => void;
  actions: {
    [K in keyof A]: ReturnType<A[K]>['payload'] extends undefined
      ? () => void
      : (payload: ReturnType<A[K]>['payload']) => void;
  };
} {
  let state = initialState;
  const listeners: ((state: S) => void)[] = [];

  const actionDispatchers = {} as any;
  for (const key in actions) {
    actionDispatchers[key] = (payload: any) => {
      const action = actions[key](payload);
      state = reducer(state, action as ActionsOf<A>);
      listeners.forEach((listener) => listener(state));
    };
  }

  return {
    getState: () => state,
    dispatch: (action: ActionsOf<A>) => {
      state = reducer(state, action);
      listeners.forEach((listener) => listener(state));
    },
    subscribe: (listener: (state: S) => void) => {
      listeners.push(listener);
      return () => {
        listeners.splice(listeners.indexOf(listener), 1);
      };
    },
    actions: actionDispatchers,
  };
}

// 테스트
interface AppState {
  count: number;
  user: string | null;
}

const actionCreators = {
  increment: (amount: number) => ({
    type: 'INCREMENT' as const,
    payload: amount,
  }),
  decrement: (amount: number) => ({
    type: 'DECREMENT' as const,
    payload: amount,
  }),
  setUser: (name: string | null) => ({
    type: 'SET_USER' as const,
    payload: name,
  }),
};

const reducer: Reducer<AppState, ActionsOf<typeof actionCreators>> = (
  state,
  action
) => {
  switch (action.type) {
    case 'INCREMENT':
      return { ...state, count: state.count + action.payload };
    case 'DECREMENT':
      return { ...state, count: state.count - action.payload };
    case 'SET_USER':
      return { ...state, user: action.payload };
    default:
      return state;
  }
};

const store = createStore(reducer, { count: 0, user: null }, actionCreators);

store.actions.increment(5); // 타입 안전
store.actions.setUser('Kim');
