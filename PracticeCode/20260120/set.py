# 1. 중괄호로 생성
fruits = {"사과", "바나나", "체리"}

# 2. set() 함수 사용
numbers = set([1-3]) # {1, 2, 3} (중복 제거됨)

# 3. 문자열로 생성 (각 문자가 요소가 됨)
chars = set("hello") # {'h', 'e', 'l', 'o'} (중복 'l' 제거됨)

# 4. 빈 집합 생성 (주의: 빈 중괄호 {}는 딕셔너리)
empty_set = set() # 빈 집합
not_set = {}      # 빈 딕셔너리, 집합 아님

# 5. 집합 컴프리헨션
squares = {x**2 for x in range(1, 6)} # {1, 4, 9, 16, 25}

# 기본 집합 생성
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# 합집합 (Union): A와 B의 모든 요소
print(A | B) # {1, 2, 3, 4, 5, 6, 7, 8}
print(A.union(B)) # 위와 동일

# 교집합 (Intersection): A와 B 모두에 있는 요소
print(A & B) # {4, 5}
print(A.intersection(B)) # 위와 동일

# 차집합 (Difference): A에는 있지만 B에 없는 요소
print(A - B) # {1, 2, 3}
print(A.difference(B)) # 위와 동일

# 대칭 차집합 (Symmetric Difference): A 또는 B에 있지만 양쪽에 모두 있지는 않은 요소
print(A ^ B) # {1, 2, 3, 6, 7, 8}
print(A.symmetric_difference(B)) # 위와 동일

# 부분집합 확인 (Subset)
C = {1, 2}
print(C.issubset(A)) # True (C는 A의 부분집합)
print(C <= A) # 위와 동일

# 진부분집합 확인 (Proper Subset)
print(C < A) # True (C는 A의 진부분집합)

# 상위집합 확인 (Superset)
print(A.issuperset(C))  # True (A는 C의 상위집합)
print(A >= C)  # 위와 동일

# 진상위집합 확인 (Proper Superset)
print(A > C)  # True (A는 C의 진상위집합)

# 서로소 확인 (Disjoint)
D = {10, 11, 12}
print(A.isdisjoint(D))  # True (A와 D는 공통 요소가 없음)

# 기본 집합
fruits = {"사과", "바나나", "체리"}

# 요소 추가
fruits.add("딸기") # {'사과', '바나나', '체리', '딸기'}

# 여러 요소 추가
fruits.update(["망고", "블루베리"]) # {'사과', '바나나', '체리', '딸기', '망고', '블루베리'}

# 요소 제거 (존재하지 않으면 오류 발생)
fruits.remove("바나나")

# 요소 제거 (존재하지 않아도 오류 없음)
fruits.discard("키위") # 없어도 오류 없음

# 임의의 요소 제거 및 반환
popped = fruits.pop() # 집합에서 임의의 요소 제거 및 반환
print(f"제거된 요소: {popped}")

# 모든 요소 제거
fruits.clear() # 빈 집합 {}

# 집합 순회
# 숫자 집합
numbers = {10, 20, 30, 40, 50}

# 기본 순회 (순서 보장되지 않음)
print("집합 요소:")
for num in numbers:
    print(num)

# 정렬된 순회가 필요하면 정렬 필요
print("\n정렬된 집합 요소:")
for num in sorted(numbers):
    print(num)

# 집합 내포 사용
squared = {x**2 for x in numbers}
print("\n제곱값 집합:", squared)

# 두 반 학생들의 취미 분석
class_a_hobbies = {"축구", "농구", "독서", "게임", "요리"}
class_b_hobbies = {"야구", "농구", "독서", "그림", "요리", "음악"}

# 양쪽 반에 모두 있는 취미 (교집합)
common_hobbies = class_a_hobbies & class_b_hobbies
print(f"공통 취미: {common_hobbies}")

# A반에만 있는 취미 (차집합)
only_a_hobbies = class_a_hobbies - class_b_hobbies
print(f"A반 전용 취미: {only_a_hobbies}")

# B반에만 있는 취미 (차집합)
only_b_hobbies = class_b_hobbies - class_a_hobbies
print(f"B반 전용 취미: {only_b_hobbies}")

# 모든 취미 목록 (합집합)
all_hobbies = class_a_hobbies | class_b_hobbies
print(f"모든 취미 목록: {all_hobbies}")

# 고유한 취미 (대칭 차집합)
unique_hobbies = class_a_hobbies ^ class_b_hobbies
print(f"한쪽 반에만 있는 취미: {unique_hobbies}")

# 취미의 종류 수
print(f"전체 취미 종류 수: {len(all_hobbies)}")

numbers = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2]

# 방법 1: 집합 변환 후 다시 리스트로 변환
unique_numbers = list(set(numbers))
print(f"중복 제거된 숫자: {unique_numbers}") # 순서 보장 안 됨

# 방법 2: 순서 유지하며 중복 제거
def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

unique_ordered = remove_duplicates(numbers)
print(f"순서 유지하며 중복 제거: {unique_ordered}")