# 1. 대괄호로 생성
fruits = ["사과", "바나나", "체리"]

# 2. list() 함수 사용
numbers = list(range(1, 6))  # [1-3, 5, 6]

# 3. 빈 리스트 생성
empty_list1 = []
empty_list2 = list()

# 4. 다양한 데이터 타입 혼합
mixed_list = [1, "안녕", 3.14, True, [1-3]]

# 5. 리스트 컴프리헨션(List Comprehension)
squares = [x**2 for x in range(1, 6)]  # [1, 5, 7-9]

# 리스트 수정
fruits = ["사과", "바나나", "체리"]

# 요소 변경
fruits[1] = "블루베리"  # ['사과', '블루베리', '체리']

# 요소 추가
fruits.append("딸기")   # ['사과', '블루베리', '체리', '딸기']

# 특정 위치에 삽입
fruits.insert(1, "포도") # ['사과', '포도', '블루베리', '체리', '딸기']

# 리스트 확장
more_fruits = ["키위", "망고"]
fruits.extend(more_fruits) # ['사과', '포도', '블루베리', '체리', '딸기', '키위', '망고']

# 요소 제거 (첫 번째 일치하는 항목)
fruits.remove("체리")   # ['사과', '포도', '블루베리', '딸기', '키위', '망고']

# 특정 위치 요소 제거 및 반환
removed = fruits.pop(2) # '블루베리' 제거 및 반환
print(removed)  # '블루베리'
print(fruits)   # ['사과', '포도', '딸기', '키위', '망고']

# 리스트 정렬
fruits.sort()   # ['망고', '딸기', '사과', '키위', '포도'] (알파벳 순)

# 리스트 역순으로 뒤집기
fruits.reverse() # ['포도', '키위', '사과', '딸기', '망고']

# 리스트 길이
print(len(fruits))  # 5

# 요소 개수 세기
fruits.append("사과")
print(fruits.count("사과")) # 2 ('사과'가 2번 등장)

# 요소 위치 찾기
print(fruits.index("키위")) # 3 ('키위'의 위치)

# 리스트 내용 비우기
fruits.clear()  # []

# enumerate 객체 변환 예시
letters = ['a', 'b', 'c']
enum_obj = enumerate(letters)
print(list(enum_obj)) # [(0, `a`), (1, `b`), (2, `c`)]

# enumerate 함수 활용하기
# 리스트 요소와 인덱스를 함께 순회할 때 유용
fruits = ["사과", "바나나", "체리", "딸기"]
for index, fruit in enumerate(fruits):
    print(f"{index}번: {fruit}") # '0번: 사과', '1번: 바나나' 등 출력

# 시작 인덱스 지정
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}번: {fruit}") # '1번: 사과', '2번: 바나나' 등 출력

# 리스트의 특정 값 위치 찾기
colors = ["빨강", "파랑", "초록", "파랑", "노랑"]
blue_indices = [i for i, color in enumerate(colors) if color == "파랑"]
print(f"파랑의 위치: {blue_indices}") # [1, 3]

# enumerate를 사용하지 않으면?
fruits = ["사과", "바나나", "체리"]
for i in range(len(fruits)):
    print(f"{i}번: {fruits[i]}")