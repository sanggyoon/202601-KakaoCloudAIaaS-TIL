// 비순수 함수 1
let total = 0;
function addToTotal(amount) {
  total += amount;
  return total;
}

// 비순수 함수 2
function shuffle(arr) {
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

// 비순수 함수 3
const config = { debug: false };
function log(message) {
  if (config.debug) {
    console.log(message);
  }
}

//TODO: 순수 함수 버전 구현
// 순수 함수 1
function add(a, b) {
  return a + b;
}

// 순수 함수 2
function getShuffledArray(arr) {
  const newArr = arr.slice(); // 원본 배열 복사
  for (let i = newArr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [newArr[i], newArr[j]] = [newArr[j], newArr[i]];
  }
  return newArr;
}

// 순수 함수 3
function createLogger(isDebug) {
  return function (message) {
    if (isDebug) {
      console.log(message);
    }
  };
}
