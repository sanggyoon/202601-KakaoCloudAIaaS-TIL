# 공통 관심사를 갖는 친구 응답
# 공통 관심사가 없는 친구 응답

test_data = {
    "Alice": ["음악", "영화", "독서"],
    "Bob": ["스포츠", "여행", "음악"],
    "Charlie": ["프로그래밍", "게임", "영화"],
    "David": ["요리", "여행", "사진"],
    "Eve": ["프로그래밍", "독서", "음악"],
    "Frank": ["스포츠", "게임", "요리"],
    "Grace": ["영화", "여행", "독서"]
}

def have_common_interest(myName, data):
  for name, favorite in data.items():
    if (name != myName):
      common_interest = set(favorite) & set(test_data[myName])
      if (len(common_interest) >= 1):
        print(f"{myName}과 {name}은 공통 관심사를 갖습니다.")

def no_common_interest(myName, data):
  for name, favorite in data.items():
    if (set(favorite).isdisjoint(set(test_data[myName]))):
      print(f"{myName}과 {name}은 공통 관심사가 없습니다.")