class BankAccount:
    interest_rate = 0.01

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance  = balance
        self.transaction_history = []

        self._log_transaction("계좌 개설", balance)

    def deposit(self, amount):
        if amount <= 0:
            print ("입금액은 0보다 커야합니다.")
            return False
        
        self.balance += amount
        self._log_transaction("입금", amount)
        print(f"{amount:,}원이 입금되었습니다. 현재 잔액: {self.balance:,}원")
        return True
    
    def withdraw(self, amount):
        if amount <= 0:
            print("출금액은 0보다 커야합니다.")
            return False

        if amount > self.balance:
            print(f"잔액 부족. 현재 잔액: {self.balance:,}원")
            return False
        
        self.balance -= amount
        self._log_transaction("출금", amount)
        print(f"{amount:,}원이 출금되었습니다. 현재 잔액: {self.balance:,}원")

    def get_balance(self):
        print(f"{self.owner}님의 계좌 잔액: {self.balance:,}원")
        return self.balance
    
    def apply_interest(self):
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest

        self._log_transaction("이자", interest)
        print(f"이자 {interest:,.2f}원이 추가되었습니다. 현재 잔액: {self.balance:,}원")

    def _log_transaction(self, transaction_type, amount):
        import datetime

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.transaction_history.append({
            "type": transaction_type,
            "amount": amount,
            "timestamp": timestamp,
            "balance": self.balance
        })

    def print_transaction_history(self):
        print(f"\n{self.owner}님의 거래 내역:")
        print("-" * 60)
        print(f"{'일시':<20} {'종류':<10} {'금액':<15} {'잔액':<15}")
        print("-" * 60)  

        for transaction in self.transaction_history:  
            print(f"{transaction['timestamp']:<20} "
              f"{transaction['type']:<10} "
              f"{transaction['amount']:,}원".ljust(15) + 
              f"{transaction['balance']:,}원".ljust(15))
        print("-" * 60)  

# 1. 계좌 생성
# 초기 잔액을 지정하거나 기본값(0)을 사용하여 인스턴스를 생성합니다.
my_account = BankAccount("홍길동", 1000000)
your_account = BankAccount("김철수")

# 2. 계좌 조작
my_account.get_balance()      # 결과: 홍길동님의 계좌 잔액: 1,000,000원
my_account.deposit(500000)    # 결과: 500,000원이 입금되었습니다. 현재 잔액: 1,500,000원
my_account.withdraw(200000)   # 결과: 200,000원이 출금되었습니다. 현재 잔액: 1,300,000원
my_account.withdraw(2000000)  # 결과: 잔액 부족. 현재 잔액: 1,300,000원

# 3. 이자 적용
# 클래스 변수 interest_rate(0.01)를 기준으로 이자를 계산하여 합산합니다.
my_account.apply_interest()   # 결과: 이자 13,000.00원이 추가되었습니다. 현재 잔액: 1,313,000원

# 4. 거래 내역 출력
# 지금까지의 모든 활동 로그를 표 형식으로 출력합니다.
my_account.print_transaction_history()