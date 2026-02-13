import { useState } from 'react';
import { useRef } from 'react';
import { useEffect } from 'react';
import './App.css';

function App() {
  // 폼 데이터 관리 ====================================================
  const [formdata, setformdata] = useState({
    username: '',
    email: '',
    password: '',
    confirmPassword: '',
  });

  const handleChange = (idname) => (event) => {
    const value = event.target.value;

    setformdata((prevState) => ({
      ...prevState,
      [idname]: value,
    }));
  };

  // Undo, Redo, History가 있는 counter ====================================================
  function useHistoryState(initialValue) {
    const pastRef = useRef([]);
    const futureRef = useRef([]);

    const [state, setState] = useState(initialValue);
    const [canUndo, setCanUndo] = useState(false);
    const [canRedo, setCanRedo] = useState(false);

    const setUpdateWithHistory = (val) => {
      pastRef.current.push(state);
      futureRef.current = [];
      setState(val);
      setCanRedo(false);
      setCanUndo(true);
    };

    const undo = () => {
      if (pastRef.current.length === 0) return;
      const previousValue = pastRef.current.pop();
      futureRef.current.push(state);
      setState(previousValue);
      setCanRedo(true);
      setCanUndo(pastRef.current.length > 0);
    };

    const redo = () => {
      if (futureRef.current.length === 0) return;
      const nextValue = futureRef.current.pop();
      pastRef.current.push(state);
      setState(nextValue);
      setCanUndo(true);
      setCanRedo(futureRef.current.length > 0);
    };

    return {
      value: state,
      setValue: setUpdateWithHistory,
      undo,
      redo,
      canUndo,
      canRedo,
    };
  }

  const { value, setValue, undo, redo, canUndo, canRedo } = useHistoryState(0);

  // 렌더링 횟수 카운터 ====================================================
  function useRenderCount() {
    // TODO: 구현하세요
    const rendering = useRef(0);
    rendering.current += 1;
    return rendering.current;
  }

  const [rand, setRand] = useState(0);

  // 사용
  // function MyComponent() {
  //   const renderCount = useRenderCount();
  //   console.log(`렌더링 횟수: ${renderCount}`);
  // }

  const renderCountNum = useRenderCount();

  // 이전 props와 변경된 props 비교 ====================================================
  function useWhyDidYouUpdate(props) {
    const previousProps = useRef(null);

    useEffect(() => {
      if (previousProps.current) {
        const changes = {};

        for (const key in props) {
          if (previousProps.current[key] !== props[key]) {
            changes[key] = {
              from: previousProps.current[key],
              to: props[key],
            };
          }
        }

        console.log('changedProps', changes);
      }

      previousProps.current = props;
    });
  }

  useWhyDidYouUpdate({ rand });

  // 사용
  // function MyComponent(props) {
  //   useWhyDidYouUpdate('MyComponent', props);
  //   // 콘솔: [MyComponent] 변경된 props: { count: { from: 1, to: 2 } }
  // }

  // useInterval 구현 ====================================================
  function useInterval(callback, delay) {
    const savedCallback = useRef();

    // 최신 콜백을 저장
    useEffect(() => {
      savedCallback.current = callback;
    }, [callback]);

    // 설정된 간격마다 콜백 실행
    useEffect(() => {
      if (delay === null) return;

      function tick() {
        savedCallback.current();
      }

      const id = setInterval(tick, delay);
      return () => clearInterval(id);
    }, [delay]);
  }

  const [count, setCount] = useState(0);
  const [delay, setDelay] = useState(1000);

  useInterval(() => {
    setCount((c) => c + 1);
  }, delay);

  // 사용 예시
  // function Timer() {
  //   const [count, setCount] = useState(0);
  //   const [delay, setDelay] = (useState < number) | (null > 1000);

  //   useInterval(() => {
  //     setCount((c) => c + 1);
  //   }, delay);
  // }

  return (
    <>
      <form
        style={{ border: '1px solid black', padding: '25px', margin: '25px' }}
      >
        <div>이름</div>
        <input
          value={formdata.username}
          onChange={handleChange('username')}
          id="username"
          type="text"
        />
        <br />
        <span>{formdata.username}</span>

        <div>이메일</div>
        <input
          value={formdata.email}
          onChange={handleChange('email')}
          id="email"
          type="email"
        />
        <br />
        <span>{formdata.email}</span>

        <div>비밀번호</div>
        <input
          value={formdata.password}
          onChange={handleChange('password')}
          id="password"
          type="password"
        />
        <br />
        <span>{formdata.password}</span>

        <div>비밀번호 확인</div>
        <input
          value={formdata.confirmPassword}
          onChange={handleChange('confirmPassword')}
          id="confirmPassword"
          type="text"
        />
        <br />
        <span>{formdata.confirmPassword}</span>
      </form>

      {/* ==================================================== */}

      <div
        style={{ border: '1px solid black', padding: '25px', margin: '25px' }}
      >
        <p>값: {value}</p>
        <button onClick={() => setValue(value + 1)}>+1</button>
        <button onClick={undo} disabled={!canUndo}>
          Undo
        </button>
        <button onClick={redo} disabled={!canRedo}>
          Redo
        </button>
      </div>

      {/* ==================================================== */}
      <div
        style={{ border: '1px solid black', padding: '25px', margin: '25px' }}
      >
        <span>렌더링 횟수: {renderCountNum / 2}</span>
        <br />
        <span>랜덤: {rand}</span>
        <br />
        <button onClick={() => setRand(Math.random())}>
          Random Number for Rerendering
        </button>
      </div>

      {/* ==================================================== */}
      <div
        style={{ border: '1px solid black', padding: '25px', margin: '25px' }}
      >
        <span>프롭스 변경은 콘솔 확인</span>
      </div>

      {/* ==================================================== */}
      <div
        style={{ border: '1px solid black', padding: '25px', margin: '25px' }}
      >
        <p>Count: {count}</p>
        <button onClick={() => setDelay(delay ? null : 1000)}>
          {delay ? '정지' : '시작'}
        </button>
        <button onClick={() => setDelay((d) => (d ? d / 2 : 1000))}>
          속도 2배
        </button>
      </div>
    </>
  );
}

export default App;
