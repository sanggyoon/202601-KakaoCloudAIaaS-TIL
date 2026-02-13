function createEventEmitter() {
  const eventMap = {
    hello: handler,
  };

  return {
    //TODO: 구현하세요
    // - on(event, callback): 이벤트 구독
    on: (event, callback) => {
      eventMap[event] = callback;
    },
    // - off(event, callback): 구독 해제
    off: (event, callback) => {
      eventMap[event] == null;
    },
    // - emit(event, ...args): 이벤트 발생
    emit: (event, ...args) => {
      eventMap[event](args);
    },
    // - once(event, callback): 한 번만 실행
    once: function (event, callback) {
      this.on(event, callback);
      this.off(event, () => {
        callback();
        this.off(event, callback);
      });
    },
  };
}

// function createEventEmitter() {
//   const eventMap = {};

//   return {
//     on(event, callback) {
//       if (!eventMap[event]) {
//         eventMap[event] = [];
//       }
//       eventMap[event].push(callback);
//     },

//     off(event, callback) {
//       if (!eventMap[event]) return;

//       eventMap[event] = eventMap[event].filter(
//         (handler) => handler !== callback
//       );
//     },

//     emit(event, ...args) {
//       if (!eventMap[event]) return;

//       eventMap[event].forEach((handler) => {
//         handler(...args);
//       });
//     },

//     once(event, callback) {
//       const wrapper = (...args) => {
//         callback(...args);
//         this.off(event, wrapper);
//       };

//       this.on(event, wrapper);
//     },
//   };
// }

// 테스트
const emitter = createEventEmitter();

const handler = (data) => console.log('Received:', data);

emitter.on('message', handler);
emitter.emit('message', 'Hello'); // "Received: Hello"
emitter.emit('message', 'World'); // "Received: World"

emitter.off('message', handler);
emitter.emit('message', 'Silent'); // (출력 없음)

emitter.once('login', (user) => console.log('Welcome:', user));
emitter.emit('login', 'Kim'); // "Welcome: Kim"
emitter.emit('login', 'Lee'); // (출력 없음)
