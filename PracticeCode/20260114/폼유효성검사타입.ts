interface ValidationRule<T> {
  validate: (value: T) => boolean;
  message: string;
}

// 1. 필드별 유효성 규칙 타입
type ValidationRules<T> = {
  [K in keyof T]?: ValidationRule<T[K]>[];
};

// 2. 유효성 검사 결과 타입
type ValidationResult<T> = {
  [K in keyof T]?: string[]; // 에러 메시지 배열
};

// 3. 폼 상태 타입
type FormState<T> = {
  values: T;
  errors: ValidationResult<T>;
  touched: { [K in keyof T]?: boolean };
  isValid: boolean;
  isDirty: boolean;
};

// 4. 폼 관리자 구현
class FormManager<T extends Record<string, any>> {
  private state: FormState<T>;
  private rules: ValidationRules<T>;

  constructor(initialValues: T, rules: ValidationRules<T>) {
    // 구현하세요
    this.state = {
      values: initialValues,
      errors: {} as ValidationResult<T>,
      touched: {},
      isValid: false,
      isDirty: false,
    };
    this.rules = rules;
  }

  setValue<K extends keyof T>(field: K, value: T[K]): void {
    // 구현하세요
    this.state = {
      ...this.state,
      values: { ...this.state.values, [field]: value },
      isDirty: true,
    };
  }

  validate(): boolean {
    // 구현하세요
    const errors: ValidationResult<T> = {};
    let isValid = true;

    for (const field in this.rules) {
      const fieldRules = this.rules[field as keyof T];
      const value = this.state.values[field as keyof T];

      if (fieldRules) {
        for (const rule of fieldRules) {
          if (!rule.validate(value)) {
            if (!errors[field as keyof T]) {
              errors[field as keyof T] = [];
            }
            errors[field as keyof T]!.push(rule.message);
            isValid = false;
          }
        }
      }
    }

    this.state = {
      ...this.state,
      errors,
      isValid,
    };

    return isValid;
  }

  getState(): Readonly<FormState<T>> {
    // 구현하세요
    return this.state;
  }
}
