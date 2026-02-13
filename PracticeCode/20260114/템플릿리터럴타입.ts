// 1. CSS 클래스 이름 생성
type Size = 'sm' | 'md' | 'lg';
type Color = 'primary' | 'secondary' | 'danger';
type Variant = 'solid' | 'outline' | 'ghost';

type ButtonClass = `btn-${Size}-${Color}-${Variant}`;
// "btn-sm-primary-solid" | "btn-sm-primary-outline" | ...

// 2. 이벤트 이름 파싱
type ParseEventName<T extends string> = T extends `on${infer Event}`
  ? Uncapitalize<Event>
  : never;

type A = ParseEventName<'onClick'>; // "click"
type B = ParseEventName<'onMouseOver'>; // "mouseOver"

// 3. 객체 경로 타입 (점 표기법)
type PathOf<T, Prefix extends string = ''> = {
  [K in keyof T]: T[K] extends object
    ? PathOf<T[K], `${Prefix}${Prefix extends '' ? '' : '.'}${K & string}`>
    : `${Prefix}${Prefix extends '' ? '' : '.'}${K & string}`;
}[keyof T];

interface Config {
  server: {
    host: string;
    port: number;
  };
  database: {
    url: string;
    name: string;
  };
}

type ConfigPath = PathOf<Config>;
// "server.host" | "server.port" | "database.url" | "database.name"
