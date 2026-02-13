# 일반 함수
def square(x):
    """입력값을 제곱하여 반환하는 일반적인 함수 정의 방식"""
    return x ** 2

# 람다 함수
# lambda 매개변수: 표현식 형태로 작성하며 이름 없이 한 줄로 정의 가능합니다.
square_lambda = lambda x: x ** 2

# 결과 확인
print(square(5))         # 출력: 25
print(square_lambda(5))  # 출력: 25

# 1. 조건식을 포함하는 람다 함수
# lambda 매개변수: 식1 if 조건 else 식2
# 두 수 중 더 큰 값을 반환하는 로직입니다.
get_max = lambda a, b: a if a > b else b

print(get_max(10, 5))  # 출력: 10


# 2. 여러 매개변수를 받는 람다 함수
# 여러 개의 매개변수를 쉼표(,)로 구분하여 선언할 수 있습니다.
# 사각형의 넓이를 계산하는 로직 ($width \times height$)입니다.
calc_rectangle_area = lambda width, height: width * height
print(calc_rectangle_area(5, 3)) # 출력: 15

# 1. map과 람다 함수 활용
# numbers 리스트의 모든 요소를 제곱하여 새로운 리스트를 생성합니다.
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))

print(squares) # 출력: [1, 4, 9, 16, 25]

# 1. filter와 람다 함수 활용
# numbers 리스트([1, 2, 3, 4, 5])에서 짝수만 골라내어 새로운 리스트를 생성합니다.
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers) # 출력: [2, 4]

# 1. reduce와 람다 함수 활용
# functools 모듈에서 reduce를 불러와야 사용 가능합니다.
from functools import reduce

# numbers 리스트([1, 2, 3, 4, 5])의 모든 요소를 곱한 결과를 계산합니다.
product = reduce(lambda x, y: x * y, numbers)

print(product) # 출력: 120 (1*2*3*4*5) 