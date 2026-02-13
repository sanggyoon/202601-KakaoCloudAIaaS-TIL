import json

# 1. 딕셔너리를 JSON 문자열로 변환 (Serialization)
person = {
    'name': '홍길동',
    'age': 30,
    'skills': ['Python', 'JavaScript'],
    'active': True
}

# json.dumps(): 파이썬 객체를 JSON 형태의 문자열로 바꿉니다.
# ensure_ascii=False: 한글이 깨지지 않고 정상적으로 표시되게 합니다.
# indent=2: 가독성을 위해 2칸 들여쓰기를 적용합니다.
json_str = json.dumps(person, ensure_ascii=False, indent=2)

print(f"JSON 문자열:\n{json_str}")

# 2. JSON 문자열을 딕셔너리로 변환 (Deserialization)
# json.loads(): JSON 형식의 문자열을 다시 파이썬 딕셔너리로 바꿉니다.
person_dict = json.loads(json_str)

print(f"이름: {person_dict['name']}, 나이: {person_dict['age']}")

import json

# 1. JSON 파일 저장
# 'w' 모드(쓰기 모드)로 파일을 생성하거나 엽니다.
with open('person.json', 'w', encoding='utf-8') as f:
    # json.dump(): 파이썬 객체를 파일 객체(f)에 JSON 형식으로 직접 저장합니다.
    # ensure_ascii=False: 한글 문자가 깨지지 않도록 설정합니다.
    # indent=2: 데이터 구조를 파악하기 쉽게 들여쓰기를 추가합니다.
    json.dump(person, f, ensure_ascii=False, indent=2)

# 2. JSON 파일 로드
# 'r' 모드(읽기 모드)로 파일을 엽니다.
with open('person.json', 'r', encoding='utf-8') as f:
    # json.load(): 파일에서 JSON 데이터를 읽어 파이썬 객체로 변환합니다.
    loaded_person = json.load(f)

print(f"파일에서 로드한 사람: {loaded_person}")