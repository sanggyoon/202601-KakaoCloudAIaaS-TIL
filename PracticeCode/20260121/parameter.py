# 필수 매개변수
def greet(name):
    return f"안녕하세요, {name}님!"

# 함수 호출 (name은 필수이므로 반드시 제공해야 함)
print(greet("철수"))  # 출력: 안녕하세요, 철수님!
# print(greet())     # 오류 발생: name 매개변수가 필요함

# 기본값 매개변수
def greet_with_time(name, time="아침"):
    return f"{time}에 만나서 반가워요, {name}님!"

# 함수 호출 (time은 기본값이 있으므로 생략 가능)
print(greet_with_time("영희"))          # 출력: 아침에 만나서 반가워요, 영희님!
print(greet_with_time("민수", "저녁"))  # 출력: 저녁에 만나서 반가워요, 민수님!

# 가변 매개변수 (*args)
def sum_all(*numbers):
    """여러 숫자의 합을 계산하는 함수"""
    # 전달된 인자들은 'numbers'라는 튜플(tuple) 형태로 묶여 들어옵니다.
    return sum(numbers)

# 함수 호출 (인자 개수 제한 없음)
# 3개의 인자를 전달하는 경우
print(sum_all(1, 2, 3))        # 출력: 6

# 5개의 인자를 전달하는 경우
print(sum_all(1, 2, 3, 4, 5))  # 출력: 15

# 인자를 하나도 전달하지 않는 경우
# 빈 튜플의 합은 0이므로 오류 없이 0을 반환합니다.
print(sum_all())               # 출력: 0 (인자가 없어도 오류 없음)

# 복합 예제: 가변 매개변수와 일반 매개변수 함께 사용
def make_pizza(size, *toppings):
    """피자 주문 정보를 출력하는 함수"""
    # 첫 번째 인자는 size 매개변수에 할당됩니다.
    print(f"{size}인치 피자를 만듭니다.")
    
    # 두 번째 인자부터는 toppings라는 튜플로 묶여 처리됩니다.
    for topping in toppings:
        print(f"- {topping} 추가")

# 함수 호출
# 12는 size로, 나머지 문자열들은 toppings로 전달됩니다.
make_pizza(12, "페퍼로니", "치즈", "올리브")

# 출력 결과:
# 12인치 피자를 만듭니다.
# - 페퍼로니 추가
# - 치즈 추가
# - 올리브 추가

# 키워드 매개변수 (**kwargs)
def create_profile(name, age, **details):
    """사용자 프로필을 생성하는 함수"""
    # 기본 정보를 담은 딕셔너리를 생성합니다.
    profile = {"name": name, "age": age}
    
    # **details로 전달된 키워드 인자들을 기존 딕셔너리에 추가합니다.
    profile.update(details)
    
    return profile

# 함수 호출 (추가 정보는 키=값 형태로 전달)
# '직업'과 '취미'가 details 딕셔너리에 담겨 전달됩니다.
print(create_profile("지원", 25, 직업="개발자", 취미="독서"))
# 출력: {'name': '지원', 'age': 25, '직업': '개발자', '취미': '독서'}

# 더 많은 정보나 리스트 형태의 데이터도 자유롭게 전달 가능합니다.
print(create_profile("민준", 30, 전공="컴퓨터공학", 거주지="서울", 언어=["Python", "Java"]))
# 출력: {'name': '민준', 'age': 30, '전공': '컴퓨터공학', '거주지': '서울', '언어': ['Python', 'Java']}

# 키워드 매개변수 (**kwargs)
def create_profile(name, age, **details):
    """사용자 프로필을 생성하는 함수"""
    # 이름과 나이를 포함한 기본 프로필 딕셔너리를 생성합니다.
    profile = {"name": name, "age": age}
    
    # **details에 담긴 추가 키워드 인자들을 기존 딕셔너리에 합칩니다.
    profile.update(details)
    
    return profile

# 함수 호출 (추가 정보는 키=값 형태로 전달)
# '직업'과 '취미'가 details 딕셔너리로 묶여 함수 내부로 전달됩니다.
print(create_profile("지원", 25, 직업="개발자", 취미="독서"))
# 출력: {'name': '지원', 'age': 25, '직업': '개발자', '취미': '독서'}

# 문자열 외에도 리스트 등 다양한 자료형을 키워드 인자로 전달할 수 있습니다.
print(create_profile("민준", 30, 전공="컴퓨터공학", 거주지="서울", 언어=["Python", "Java"]))
# 출력: {'name': '민준', 'age': 30, '전공': '컴퓨터공학', '거주지': '서울', '언어': ['Python', 'Java']}

def complex_function(required, optional="기본값", *args, **kwargs):
    """여러 종류의 매개변수를 모두 사용하는 함수"""
    # 필수 매개변수 출력
    print(f"필수 매개변수: {required}")
    # 기본값이 설정된 선택적 매개변수 출력
    print(f"선택적 매개변수: {optional}")
    # 전달된 모든 위치 인자들을 튜플로 출력
    print(f"가변 위치 매개변수: {args}")
    # 전달된 모든 키워드 인자들을 딕셔너리로 출력
    print(f"가변 키워드 매개변수: {kwargs}")

# 함수 호출
# 순서대로: required, optional, *args(1,2,3), **kwargs(키워드1, 키워드2)
complex_function("필수값", "선택값", 1, 2, 3, 키워드1="값1", 키워드2="값2")

# 출력 결과:
# 필수 매개변수: 필수값
# 선택적 매개변수: 선택값
# 가변 위치 매개변수: (1, 2, 3)
# 가변 키워드 매개변수: {'키워드1': '값1', '키워드2': '값2'}

# 올바른 매개변수 순서
# 필수 매개변수 -> 기본값 매개변수 -> 가변 위치 매개변수(*args) -> 가변 키워드 매개변수(**kwargs)
def correct_order(normal, default="기본값", *args, **kwargs):
    pass

# 잘못된 매개변수 순서 (오류 발생)
# 가변 키워드 매개변수(**kwargs)가 가변 위치 매개변수(*args)보다 앞에 오면 안 됩니다.
# def wrong_order(**kwargs, *args): # SyntaxError: invalid syntax
#     pass

def function_demo(*args, **kwargs):
    # 각 매개변수의 타입과 실제 값을 출력하여 구조를 확인합니다.
    print(f"args 타입: {type(args)}, 값: {args}")
    print(f"kwargs 타입: {type(kwargs)}, 값: {kwargs}")

    # args 접근 방식: 튜플이므로 인덱스를 사용하여 접근합니다.
    if args:
        print("args의 첫 번째 값:", args[0])

    # kwargs 접근 방식: 딕셔너리이므로 키(key)를 사용하여 접근합니다.
    if 'name' in kwargs:
        print("이름:", kwargs['name'])

# 함수 호출 예시
# 1, 2, 3은 args로, name과 age는 kwargs로 전달됩니다.
function_demo(1, 2, 3, name="홍길동", age=30)

# --- 출력 결과 ---
# args 타입: <class 'tuple'>, 값: (1, 2, 3)
# kwargs 타입: <class 'dict'>, 값: {'name': '홍길동', 'age': 30}
# args의 첫 번째 값: 1
# 이름: 홍길동