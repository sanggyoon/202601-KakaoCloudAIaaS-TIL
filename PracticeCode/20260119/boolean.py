print(bool(0))        # False
print(bool(1))        # True
print(bool(-1))       # True (0이 아닌 모든 숫자는 True)
print(bool(""))       # False (빈 문자열)
print(bool("Hello"))  # True (비어있지 않은 문자열)
print(bool([]))       # False (빈 리스트)
print(bool([1, 2]))   # True (비어있지 않은 리스트)
print(bool(None))     # False

# 논리 연산자
x = True
y = False

print(x and y)  # False (둘 다 True일 때만 True)
print(x or y)   # True (둘 중 하나라도 True면 True)
print(not x)    # False (부정)

# 단축 평가(Short-circuit evaluation)
# and 연산자: 첫 값이 False면 두 번째 값은 평가하지 않고 바로 False 반환
print(False and print("확인"))  # False (print 함수 실행되지 않음)

# or 연산자: 첫 값이 True면 두 번째 값은 평가하지 않고 바로 True 반환
print(True or print("확인"))    # True (print 함수 실행되지 않음)

# 실제 값 반환
print(0 and 5)   # 0 (첫 번째 값이 False이므로 0 반환)
print(2 and 5)   # 5 (첫 번째 값이 True이므로 두 번째 값 반환)
print(0 or 5)    # 5 (첫 번째 값이 False이므로 두 번째 값 반환)
print(2 or 5)    # 2 (첫 번째 값이 True이므로 첫 번째 값 반환)

# 비교 연산
equal = (5 == 5)        # True
not_equal = (5 != 3)    # True
greater = (5 > 3)       # True
less = (5 < 3)          # False

# 복합 비교 연산
x = 10
complex_check = (5 < x < 15)  # True (5 < 10 and 10 < 15)

# 객체 비교
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 == list2)   # True (내용이 같음)
print(list1 is list2)   # False (다른 객체)
print(list1 is list3)   # True (같은 객체)

# 정수로 변환
int("123")    # 123
int(3.14)     # 3
int(True)     # 1

# 실수로 변환
float("3.14") # 3.14
float(5)      # 5.0
float(True)   # 1.0

# 문자열로 변환
str(123)      # "123"
str(3.14)     # "3.14"
str(True)     # "True"

# 불리언으로 변환
bool(1)       # True
bool(0)       # False
bool("Hello") # True
bool("")      # False

# 문제 1: 다음 코드의 출력 결과는 무엇인가요?
a = 0.1 + 0.1 + 0.1
b = 0.3
print(a == b)

# 문제 2: 다음 중 False로 평가되지 않는 것은 무엇인가요?
# a) 0
# b) ""
# c) 
# d) None
# e) False

# 문제 3: 다음 코드의 실행 결과와 그 이유를 설명하세요.
text = "Python"
text = "J"
print(text)