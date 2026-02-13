//TODO: 오버로드 시그니처를 작성하세요

// 1. createElement 함수
// - ("div") => HTMLDivElement
// - ("span") => HTMLSpanElement
// - ("input") => HTMLInputElement
// - (string) => HTMLElement
//
function createElement(tag: 'div'): HTMLDivElement;
function createElement(tag: 'span'): HTMLSpanElement;
function createElement(tag: 'input'): HTMLInputElement;
function createElement(tag: string): HTMLElement;

function createElement(
  tag: string | 'div' | 'span' | 'input'
): HTMLElement | HTMLDivElement | HTMLSpanElement | HTMLInputElement {
  return document.createElement(tag);
}

// 2. fetch 함수
// - (url: string) => Promise<Response>
// - (url: string, options: RequestOptions) => Promise<Response>
// - (request: Request) => Promise<Response>

interface RequestOptions {
  method?: string;
  headers?: Record<string, string>;
  body?: string;
}

//TODO: 오버로드 정의
function fetch(url: string): Promise<Response>;
function fetch(url: string, options: RequestOptions): Promise<Response>;
function fetch(requeset: Request): Promise<Response>;

function fetch(
  input: string | Request,
  init?: RequestOptions
): Promise<Response> {
  return window.fetch(input, init);
}

// 3. 배열/단일 값 처리 함수
// - process(item: T) => T
// - process(items: T[]) => T[]

//TODO: 오버로드 정의
function process<T>(item: T): T;
function process<T>(items: T[]): T[];

function process<T>(input: T | T[]): T | T[] {
  return input;
}
