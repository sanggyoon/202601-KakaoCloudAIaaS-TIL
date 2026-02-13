let wide: string;
let narrow: 'kim' = 'kim';

wide = narrow; // wide의 값은 "kim", 타입은 string

let superWide: unknown = 'kim';
let superNarrow: never;

superWide = wide; // OK
superWide = narrow; // OK
superWide = superNarrow; // error

superNarrow = wide; // error
superNarrow = narrow; //error
superNarrow = superNarrow; // OK
