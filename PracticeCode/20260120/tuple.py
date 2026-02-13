# 1. 소괄호로 생성
coordinates = (10, 20)

# 2. tuple() 함수 사용
numbers = tuple([1, 2, 3, 4, 5]) # (1, 2, 3, 4, 5)

# 3. 소괄호 없이도 생성 가능
colors = "red", "green", "blue" # ('red', 'green', 'blue')

# 4. 단일 요소 튜플 (주의: 콤마 필요)
single_item = (42,) # (42,)
not_tuple = (42) # 42 (튜플이 아닌 일반 정수)

# 5. 빈 튜플 생성
empty_tuple = ()
empty_tuple2 = tuple()

# 6. 다양한 데이터 타입 혼합
mixed_tuple = (1, "안녕", 3.14, True, (1, 2, 3))

# 튜플 접근과 슬라이싱
fruits = ("사과", "바나나", "체리", "딸기", "오렌지")

# 인덱싱 (리스트와 동일)
print(fruits)    # '사과'
print(fruits[-1])   # '오렌지'

# 슬라이싱 (리스트와 동일)
print(fruits[1:4])  # ('바나나', '체리', '딸기')
print(fruits[:3])   # ('사과', '바나나', '체리')
print(fruits[::2])  # ('사과', '체리', '오렌지')

# 중첩 튜플 접근
nested = (1, 2, (3, 4, 5))
print(nested[2][1]) # 4

# 튜플 길이
print(len(fruits))  # 5

# 요소 존재 여부 확인
print("바나나" in fruits) # True

# 튜플은 변경 불가능
coordinates = (10, 20, 30)

# 아래 코드는 오류 발생
# coordinates = 100 # TypeError: 'tuple' object does not support item assignment

# 튜플 자체를 새로운 튜플로 재할당은 가능
coordinates = (100, 200, 300) # 새로운 튜플 객체 생성

# 튜플 메서드와 연산
numbers = (1, 2, 3, 2, 4, 2)

# count(): 특정 요소 개수 반환
print(numbers.count(2)) # 3 (2가 3개 있음)

# index(): 특정 요소의 첫 번째 위치 반환
print(numbers.index(3)) # 2 (3은 인덱스 2에 위치)

# 튜플 연결
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2 # (1, 2, 3, 4, 5, 6)

# 튜플 반복
repeated = tuple1 * 3 # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# 튜플 비교 (요소별 비교)
print((1, 2, 3) < (1, 3, 0)) # True (첫 번째 요소가 같아서 두 번째 요소 비교)

# 튜플 언패킹(Unpacking)
# 기본 언패킹
rgb = (255, 100, 50)
red, green, blue = rgb
print(f"Red: {red}, Green: {green}, Blue: {blue}") # Red: 255, Green: 100, Blue: 50

# 일부 요소만 언패킹
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(first)   # 1
print(middle)  # [2, 3, 5]
print(last)    # 5

# 함수에서 여러 값 반환 시 튜플 활용
def get_user_info():
    return "홍길동", 30, "서울"

name, age, city = get_user_info()
print(f"{name}은 {age}세이고 {city}에 살고 있습니다.")

# 좌표 데이터는 쉽게 변경되면 안됨
critical_coordinates = (37.5665, 126.9780)

def process_location(coord):
    # coord가 튜플이면 함수 내에서 변경될 위험 없음
    latitude, longitude = coord
    # 처리 로직...
    return 

def get_dimensions():
    width = 800
    height = 600
    depth = 3
    return width, height, depth # 암시적 튜플 반환

# 반환값을 튜플로 받기
dimensions = get_dimensions()
print(f"튜플: {dimensions}") # 튜플: (800, 600, 3)

# 언패킹으로 개별 값 받기
w, h, d = get_dimensions()
print(f"너비: {w}, 높이: {h}, 깊이: {d}") # 너비: 800, 높이: 600, 깊이: 3

# 1. 소괄호로 생성
coordinates = (10, 20)

# 2. tuple() 함수 사용
numbers = tuple([1, 2, 3, 4, 5])  # (1, 2, 3, 4, 5)

# 3. 소괄호 없이도 생성 가능
colors = "red", "green", "blue"  # ('red', 'green', 'blue')

# 4. 단일 요소 튜플 (주의: 콤마 필요)
single_item = (42,)  # (42,)
not_tuple = (42)     # 42 (튜플이 아닌 일반 정수)

# 5. 빈 튜플 생성
empty_tuple = ()
empty_tuple2 = tuple()

# 6. 다양한 데이터 타입 혼합
mixed_tuple = (1, "안녕", 3.14, True, (1, 2, 3))

from collections import namedtuple

# 네임드 튜플 정의
Person = namedtuple('Person', ['name', 'age', 'city'])

# 생성 및 사용
person1 = Person('홍길동', 30, '서울')

# 인덱스로 접근
print(person1) # 홍길동

# 필드명으로 접근 (가독성 높음)
print(person1.name) # 홍길동
print(person1.age)  # 30
print(person1.city) # 서울

def add_to_each(data, value) :
    # 원본 데이터를 변경하지 않고 새 튜플 반환
    return tuple(item + value for item in data)

nubers = (1, 2, 3)
new_numbers = add_to_each(numbers, 10)

print(numbers)      # (1. 2. 3) - 원본 그대로 유지
print(new_numbers)  # (11, 12, 13) - 새 튜플 생성