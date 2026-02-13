interface Dog {
  type: 'dog';
  name: string;
  breed: string;
  bark(): void;
}

interface Cat {
  type: 'cat';
  name: string;
  color: string;
  meow(): void;
}

interface Bird {
  type: 'bird';
  name: string;
  wingspan: number;
  fly(): void;
}

type Animal = Dog | Cat | Bird;

//TODO: 다음 타입 가드들을 구현하세요

function isDog(animal: Animal): animal is Dog {
  //TODO
  if (animal.type === 'dog') {
    return true;
  }
  return false;
}

function isCat(animal: Animal): animal is Cat {
  //TODO
  if (animal.type === 'cat') {
    return true;
  }
  return false;
}

function isBird(animal: Animal): animal is Bird {
  //TODO
  if (animal.type === 'bird') {
    return true;
  }
  return false;
}

// 범용 타입 가드
function isAnimalType<T extends Animal>(
  animal: Animal,
  type: T['type']
): animal is T {
  //TODO
  return animal.type === type;
}

// 동물 소리 내기
function makeSound(animal: Animal): void {
  //TODO: 타입 가드 사용하여 구현
  if (isDog(animal)) {
    return animal.bark();
  } else if (isCat(animal)) {
    return animal.meow();
  } else if (isBird(animal)) {
    return animal.fly();
  }
}

// 테스트
const dog: Dog = {
  type: 'dog',
  name: 'Max',
  breed: 'Labrador',
  bark: () => console.log('Woof!'),
};
const cat: Cat = {
  type: 'cat',
  name: 'Whiskers',
  color: 'orange',
  meow: () => console.log('Meow!'),
};

makeSound(dog); // Woof!
makeSound(cat); // Meow!
