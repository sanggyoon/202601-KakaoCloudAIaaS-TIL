def multiplier(n):
    """입력받은 n을 곱해주는 람다 함수를 반환합니다."""
    return lambda x: x * n

# multiplier 함수를 이용해 '2배'와 '3배' 계산기 객체를 생성합니다.
double = multiplier(2) # n=2가 고정된 람다 함수 반환
triple = multiplier(3) # n=3이 고정된 람다 함수 반환

# 생성된 함수 객체를 호출하여 결과를 확인합니다.
print(double(5)) # 출력: 10 (5 * 2)
print(triple(5)) # 출력: 15 (5 * 3)

def power_function(n):
    """입력받은 n을 지수로 사용하는 거듭제곱 함수를 반환합니다."""
    def power(x):
        # 외부 함수의 변수 n을 내부 함수인 power가 기억(Capture)합니다.
        return x ** n
    return power

# 제곱 함수 생성 (n=2인 클로저 인스턴스)
square = power_function(2)
# 세제곱 함수 생성 (n=3인 클로저 인스턴스)
cube = power_function(3)

# 생성된 함수 사용
print(square(4)) # 출력: 16 (4의 제곱)
print(cube(3))   # 출력: 27 (3의 세제곱)

# 데코레이터
def 데코레이터_함수(원본_함수):
    """원본 함수를 감싸서 추가 기능을 부여하는 데코레이터입니다."""
    
    # 래퍼 함수는 원본 함수의 인자를 유연하게 받기 위해 *args, **kwargs를 사용합니다.
    def 래퍼_함수(*args, **kwargs):
        # 1. 원본 함수 실행 전 수행할 작업 (예: 로그 기록, 권한 확인)
        print("작업 시작: 원본 함수를 실행하기 전입니다.")
        
        # 2. 원본 함수 실행
        결과 = 원본_함수(*args, **kwargs)
        
        # 3. 원본 함수 실행 후 수행할 작업 (예: 실행 시간 계산, 결과 가공)
        print("작업 종료: 원본 함수 실행이 완료되었습니다.")
        
        return 결과
        
    return 래퍼_함수

def validate_input(func):
    """입력값이 0보다 큰지 검증하는 데코레이터"""
    def wrapper(x, y):
        # 입력값 x 또는 y가 0보다 작으면 ValueError를 발생시킵니다.
        if x < 0 or y < 0:
            raise ValueError("입력값은 0보다 커야 합니다.")
        return func(x, y)
    return wrapper

@validate_input
def divide(x, y):
    """나눗셈을 수행하는 함수"""
    # 분모가 0인 경우에 대한 예외 처리를 수행합니다.
    if y == 0:
        raise ZeroDivisionError("0으로 나눌 수 없습니다.")
    return x / y

# 테스트
try:
    print(divide(10, 2))   # 출력: 5.0
    print(divide(-10, 2))  # ValueError 발생 (데코레이터에서 차단)
except ValueError as e:
    print(e)               # 출력: 입력값은 0보다 커야 합니다.