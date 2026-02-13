function createBankAccount(initialBalance) {
  //TODO: 구현하세요
  const _initBal = initialBalance;
  let balance = _initBal;
  let histories = [];

  return {
    // - deposit(amount): 입금
    deposit: (amount) => {
      balance = balance + amount;
      histories.push({
        type: 'deposit',
        amount: amount,
      });
    },
    // - withdraw(amount): 출금 (잔액 부족시 false 반환)
    withdraw: (amount) => {
      if (balance >= amount) {
        balance = balance - amount;
        histories.push({
          type: 'withdraw',
          amount: amount,
        });
        return true;
      } else {
        return false;
      }
    },
    // - getBalance(): 잔액 조회
    getBalance: () => {
      return balance;
    },
    // - getHistory(): 거래 내역 조회
    getHistory: () => {
      return [...histories];
    },
  };
}

// 테스트
const account = createBankAccount(1000);
account.deposit(500);
console.log(account.getBalance()); // 1500
console.log(account.withdraw(2000)); // false
console.log(account.withdraw(300)); // true
console.log(account.getBalance()); // 1200
console.log(account.getHistory()); // [{type: 'deposit', amount: 500}, {type: 'withdraw', amount: 300}]
