// 타입 안전 상태 관리 구현
interface Store<S> {
  getState(): S;
  setState(partial: Partial<S>): void;
  subscribe(listener: (state: S) => void): () => void;

  // 선택자 - 상태의 일부만 구독
  select<R>(selector: (state: S) => R): {
    get(): R;
    subscribe(listener: (value: R) => void): () => void;
  };
}

function createStore<S extends object>(initialState: S): Store<S> {
  // 구현하세요
  let state: S = initialState;
  const listeners: Array<(state: S) => void> = [];

  return {
    getState() {
      return state;
    },
    setState(partial: Partial<S>) {
      state = { ...state, ...partial };
      listeners.forEach((listener) => listener(state));
    },
    subscribe(listener: (state: S) => void) {
      listeners.push(listener);
      return () => {
        const index = listeners.indexOf(listener);
        if (index > -1) {
          listeners.splice(index, 1);
        }
      };
    },
    select<R>(selector: (state: S) => R) {
      let currentValue = selector(state);
      const selectedListeners: Array<(value: R) => void> = [];

      return {
        get() {
          return currentValue;
        },
        subscribe(listener: (value: R) => void) {
          selectedListeners.push(listener);
          return () => {
            const index = selectedListeners.indexOf(listener);
            if (index > -1) {
              selectedListeners.splice(index, 1);
            }
          };
        },
      };
    },
  };
}

// 테스트
interface AppState {
  user: { name: string; loggedIn: boolean } | null;
  theme: 'light' | 'dark';
  notifications: string[];
}

const store = createStore<AppState>({
  user: null,
  theme: 'light',
  notifications: [],
});

const userSelector = store.select((s) => s.user);
userSelector.subscribe((user) => {
  console.log('User changed:', user);
});

store.setState({ user: { name: 'Kim', loggedIn: true } });
