# 단일 변수 선언
name = "홍길동"
age = 25
height= 175.5
is_student = True

# 변수 선언 시 주의 사항
# 1. 변수명은 의미있게 지어야함
student_name = "김철수" # good
x = "김철수"            # bad

# 2. 변수 선언 시 초기값 설정이 좋음
score = 0     # good
# total_score   # bad

# 여러 변수 동시 선언
# 방법 1
x, y, z = 1, 2, 3

# 방법 2
a = b = c = 10

# 방법 3
numbers = [1, 2, 3]
first, second, third = numbers

# 변수 값 교환
# 일방적인 방법
a = 1
b = 2
temp = a
a = b
b = temp

# 파이썬 방식
a, b = 1, 2
a, b = b, a

# 변수 타입 특징
x = 10 
print(type(x))  # <class 'int'>

x = "hello"
print(type(x))  # <class 'str'>

x = True
print(type(x))  # <class 'bool'>

# 파이썬 변수 저장 방법
# 가변 타입의 참조는 메모리 공간을 공유하는 깊은 참조에 해당한다.
list1 = [1,2 ,3]
list2 = list1
list2 = 10
print(list2)  # 10

# 변수 스코프 (전역 변수)
global_var = "전역 변수"

def my_function():
  print(global_var) # 전역 변수 접근

print(global_var) # 전역 변수 접근

# 변수 스코프 (지역 변수)
def my_function2():
  local_var = "지역 변수"
  print(local_var)

#print(local_var) # 오류: 정의되지 않음


# 변수 스코프
count = 0

def increment():
    global count # 없다면 에러
    count += 1

increment()
print(count)  # 1

student_name = "김철수"
student_age = 20
student_height = 175.5
is_enrolled = True

# 정보 출력
print("=== 학생 정보 ===")
print(f"이름: {student_name}")
print(f"나이: {student_age}세")
print(f"키: {student_height}cm")
print(f"등록 여부: {'등록' if is_enrolled else '미등록'}")

# 실습 2: 수학 연산
x = 10
y = 3

# 기본 연산
addition = x + y
subtraction = x - y
multiplication = x * y
division = x / y
remainder = x % y

print("\n=== 수학 연산 ===")
print(f"덧셈: {x} + {y} = {addition}")
print(f"뺄셈: {x} - {y} = {subtraction}")
print(f"곱셈: {x} * {y} = {multiplication}")
print(f"나눗셈: {x} / {y} = {division}")
print(f"나머지: {x} % {y} = {remainder}")