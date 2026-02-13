# 작은 수
small = 10
print(type(small))  # <class 'int'>

# 큰 수
large = 123456789012345678901234567890
print(type(large))  # <class 'int'>

# 정밀도 제한 예시
a = 0.1 + 0.2
print(a) # 0.30000000000000004 (예상과 다른 결과)

# 정밀도 제한으로 인한 비교 문제
print(0.1 + 0.2 == 0.3) # False

# 해결 방법: 반올림 사용
print(round(0.1 + 0.2, 1) == 0.3) # True

# 1. 반올림 사용
result = round(0.1 + 0.2, 1) # 0.3

# 2. decimal 모듈 사용 (정확한 10진수 연산)
from decimal import Decimal
a = Decimal('0.1')
b = Decimal('0.2')
print(a + b) # 0.3

# 3. math 모듈의 isclose 함수 사용
import math
print(math.isclose(0.1 + 0.2, 0.3)) # True

# 복소수 생성 방법
z1 = 3 + 4j         # 직접 리터럴로 생성
z2 = complex(3, 4)  # complex() 함수로 생성

# 복소수 속성
print(z1.real)      # 3.0 (실수부)
print(z1.imag)      # 4.0 (허수부)

# 켤레복소수 (허수부의 부호를 바꾼 복소수)
print(z1.conjugate()) # (3-4j)

# 문자열 생성 방법
str1 = "Hello"
# str2 = `World` --> 백틱은 더이상 지원하지 않음
str3 = """여러 줄 문자열"""
# str4 = ```여러 줄 문자열``` 백틱은 더이상 지원하지 않음

# 문자열 불변성
text = "Hello"
text[0] = "3"   # 오류 발생

text = "Hello"
new_text = text.replace("H", "3") # ."Hello" 는 그대로, "Jello" 라는 새 문자열 생성
text += " World" # 실제로는 "Hello World" 라는 새 문자열 생성

# 문자열 연산
concatenation = "Hello" + " " + "World"  # "Hello World"
repetition = "Hi" * 3  # "HiHiHi"

# 문자열 인덱싱
text = "Python"
first_char = text   # 'P'
last_char = text[-1]   # 'n' 음수 인덱스는 문자열의 끝에서부터 셈

# 문자열 슬라이싱
substring = text[1:4]  # 'yth' 시작 인덱스 포함, 끝 인덱스는 포함하지 않음

# 문자열 변환 메서드
text = "Python Programming"
print(text.upper())     # "PYTHON PROGRAMMING"
print(text.lower())     # "python programming"
print(text.title())     # "Python Programming"
print(text.swapcase())  # "pYTHON pROGRAMMING"

# 검색 메서드
print(text.find("Pro")) # 7 (첫 번째 위치 반환, 없으면 -1)
print(text.count("m"))  # 2 (문자 출현 횟수)
print("Pro" in text)    # True (포함 여부)

# 변형 메서드
print(text.replace("Python", "Java"))  # "Java Programming"
print(" Hello ".strip())  # "Hello" (양쪽 공백 제거)
print(text.split(" "))    # ["Python", "Programming"] (분할)
print("-".join(["a", "b", "c"])) # "a-b-c" (결합)

# 검증 메서드
print("12345".isdigit())  # True (모두 숫자인지)
print("abcde".isalpha())  # True (모두 알파벳인지)
print("Python1".isalnum()) # True (알파벳 또는 숫자인지)

# f-string (Python 3.6+)
name = "홍길동"
age = 25
message = f"이름: {name}, 나이: {age}"

# format 메서드
message = "이름: {}, 나이: {}".format(name, age)