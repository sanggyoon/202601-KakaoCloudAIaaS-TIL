//TODO: 구현하세요

function myMap(arr, fn) {
  // Array.prototype.map 구현
  const result = [];
  for (let i = 0; i < arr.length; i++) {
    result.push(fn(arr[i], i, arr));
  }
  return result;
}

function myFilter(arr, predicate) {
  // Array.prototype.filter 구현
  const result = [];
  for (let i = 0; i < arr.length; i++) {
    if (predicate(arr[i], i, arr)) {
      result.push(arr[i]);
    }
  }
  return result;
}

function myReduce(arr, reducer, initialValue) {
  // Array.prototype.reduce 구현
  let accumulator = initialValue;
  let startIndex = 0;
  if (accumulator === undefined) {
    accumulator = arr[0];
    startIndex = 1;
  }
  for (let i = startIndex; i < arr.length; i++) {
    accumulator = reducer(accumulator, arr[i], i, arr);
  }
  return accumulator;
}

function myFind(arr, predicate) {
  // Array.prototype.find 구현
  for (let i = 0; i < arr.length; i++) {
    if (predicate(arr[i], i, arr)) {
      return arr[i];
    }
  }
  return undefined;
}

function myEvery(arr, predicate) {
  // Array.prototype.every 구현
  for (let i = 0; i < arr.length; i++) {
    if (!predicate(arr[i], i, arr)) {
      return false;
    }
  }
  return true;
}

function mySome(arr, predicate) {
  // Array.prototype.some 구현
  for (let i = 0; i < arr.length; i++) {
    if (predicate(arr[i], i, arr)) {
      return true;
    }
    return false;
  }
}

// 테스트
const nums = [1, 2, 3, 4, 5];

console.log(myMap(nums, (x) => x * 2)); // [2, 4, 6, 8, 10]
console.log(myFilter(nums, (x) => x % 2 === 0)); // [2, 4]
console.log(myReduce(nums, (a, b) => a + b, 0)); // 15
console.log(myFind(nums, (x) => x > 3)); // 4
console.log(myEvery(nums, (x) => x > 0)); // true
console.log(mySome(nums, (x) => x > 4)); // true
