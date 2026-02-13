//TODO: 다음 타입과 클래스들을 구현하세요

interface PaymentResult {
  success: boolean;
  transactionId?: string;
  error?: string;
}

abstract class PaymentProcessor {
  //TODO: 추상 클래스 구현
  abstract process(amount: number, currency: string): Promise<PaymentResult>;
}

class CreditCardProcessor extends PaymentProcessor {
  //TODO
  async process(amount: number, currency: string): Promise<PaymentResult> {
    return {
      success: true,
      transactionId: '',
      error: undefined,
    };
  }
}

class PayPalProcessor extends PaymentProcessor {
  //TODO
  async process(amount: number, currency: string): Promise<PaymentResult> {
    return {
      success: true,
      transactionId: '',
      error: undefined,
    };
  }
}

class CryptoProcessor extends PaymentProcessor {
  //TODO
  async process(amount: number, currency: string): Promise<PaymentResult> {
    return {
      success: true,
      transactionId: '',
      error: undefined,
    };
  }
}

// 팩토리
class PaymentFactory {
  static create(type: 'credit' | 'paypal' | 'crypto'): PaymentProcessor {
    //TODO
    switch (type) {
      case 'credit':
        return new CreditCardProcessor();
      case 'paypal':
        return new PayPalProcessor();
      case 'crypto':
        return new CryptoProcessor();
      default:
        throw new Error('Unsupported payment type');
    }
  }
}

// 테스트
const creditProcessor = PaymentFactory.create('credit');
const result = await creditProcessor.process(100, 'USD');
console.log(result);
