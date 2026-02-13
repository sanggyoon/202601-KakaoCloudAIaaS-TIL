function createCounter(initialValue = 0) {
  const _initValue = initialValue;
  let value = _initValue;

  return {
    increment: () => {
      value = value + 1;
    },
    decrement: () => {
      value = value - 1;
    },
    getValue: () => {
      return value;
    },
    reset: () => {
      return (value = initialValue);
    },
  };
}

// 테스트
const counter = createCounter(10);
const counter2 = createCounter(100);
counter.increment(); // 11
counter.increment(); // 12
console.log(counter.getValue()); // 12 출력
counter.decrement(); // 11
console.log(counter.getValue()); // 11 출력
counter.reset();
console.log(counter.getValue()); // 10 출력

counter2.increment(); // 101
console.log(counter.getValue()); // 10 츌력
console.log(counter2.getValue()); // 101 출력
