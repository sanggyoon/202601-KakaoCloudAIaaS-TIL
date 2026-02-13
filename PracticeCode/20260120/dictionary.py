import time

# 데이터 준비
data_size = 1000000 # 백만 개의 데이터
search_key = f"key_{data_size-1}" # 마지막 요소 검색 (최악의 경우)

# 딕셔너리 생성
dict_data = {f"key_{i}": i for i in range(data_size)}

# 리스트 생성
list_data = [(f"key_{i}", i) for i in range(data_size)]

# 딕셔너리 검색 (O(1)) 시간 측정
start_time = time.time()
result_dict = dict_data[search_key]
dict_time = time.time() - start_time
# 1. 중괄호와 콜론으로 생성
student = {"name": "홍길동", "age": 20, "grade": "A"}

# 2. dict() 함수 사용
student2 = dict(name="김철수", age=22, grade="B")

# 3. 키-값 튜플의 리스트로 생성
items = [("name", "이영희"), ("age", 25), ("grade", "C")]
student3 = dict(items)

# 4. 빈 딕셔너리 생성
empty_dict = {}
empty_dict2 = dict()

# 5. dict.fromkeys() 사용 (여러 키에 동일한 값 할당)
keys = ["name", "age", "grade"]
default_student = dict.fromkeys(keys, "미정") # {'name': '미정', 'age': '미정', 'grade': '미정'}

# 딕셔너리 접근과 수정
person = {
    "name": "홍길동",
    "age": 30,
    "city": "서울",
    "skills": ["Python", "Java", "SQL"]
}

# 값 접근
print(person["name"])      # '홍길동'
print(person.get("age"))   # 30

# get() 메서드의 장점: 키가 없을 때 에러 대신 기본값 반환
print(person.get("email", "이메일 없음")) # '이메일 없음'

# 값 수정
person["age"] = 31

# 새 항목 추가
person["email"] = "hong@example.com"

# 항목 삭제
del person["city"] # 키로 삭제

# 다른 삭제 방법
skill = person.pop("skills") # 키를 지정하여 값 반환 후 삭제
print(f"제거된 skills: {skill}")

# 딕셔너리 메서드
student = {
    "name": "홍길동",
    "age": 20,
    "courses": ["수학", "영어", "과학"]
}

# keys(): 모든 키 반환
print(list(student.keys())) # ['name', 'age', 'courses']

# values(): 모든 값 반환
print(list(student.values())) # ['홍길동', 20, ['수학', '영어', '과학']]

# items(): 키-값 쌍 반환
print(list(student.items())) # [('name', '홍길동'), ('age', 20), ('courses', ['수학', '영어', '과학'])]

# update(): 딕셔너리 병합/갱신
new_info = {"grade": "A", "age": 21}
student.update(new_info)
print(student) # {'name': '홍길동', 'age': 21, 'courses': ['수학', '영어', '과학'], 'grade': 'A'}

# clear(): 모든 항목 삭제
temp_dict = {"temp": 1}
temp_dict.clear()
print(temp_dict) # {}

# copy(): 딕셔너리 얕은 복사
student_copy = student.copy()

# 딕셔너리 순회
student = {
    "name": "홍길동",
    "age": 20,
    "grade": "A",
    "courses": ["수학", "영어", "과학"]
}

# 키 순회
print("*** 키 목록 ***")
for key in student: # student_key() 와 동일
    print(key)

# 값 순회
print("*** 값 목록 ***")
for value in student.values():
    print(value)

# 키-값 쌍 순회
print("*** 키-값 쌍 ***")
for key, value in student.item():
    print(f"(key): (value)")

# 중첩 딕셔너리
users = {
    "user1": {
        "name": "홍길동",
        "age": 30,
        "email": "hong@example.com"
    },
    "user2": {
        "name": "김철수",
        "age": 25,
        "email": "kim@example.com"
    }
}

# 중첩 값 접근
print(users["user1"]["name"]) # '홍길동'

# 중첩 딕셔너리 순회
for user_id, user_info in users.items():
    print(f"\n사용자 ID: {user_id}")
    for key, value in user_info.items():
        print(f"  {key}: {value}")

# 딕셔너리 컴프리헨션
# 1. 기본 형태
squares = {x: x**2 for x in range(1, 6)}
print(squares) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2. 조건부 딕셔너리 컴프리헨션
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares) # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# 3. 값 변환 예제
fruits = ['apple', 'banana', 'cherry']
fruit_lengths = {fruit: len(fruit) for fruit in fruits}
print(fruit_lengths) # {'apple': 5, 'banana': 6, 'cherry': 6}