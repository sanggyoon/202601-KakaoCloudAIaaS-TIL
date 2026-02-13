type StringToLength<T> = T extends string ? number : T;
// T가 string에 할당 가능하면 number 반환, 아니면 T
