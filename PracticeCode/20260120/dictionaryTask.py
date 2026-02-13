# 딕셔너리를 활용하여 간단한 주소록 프로그램 작성
# 연락처 이름을 키로 하고, 전화번호, 이메일, 주소 등의 정보를 값으로 저장
# 중첩 딕셔너리 구조를 사용하여 연락처마다 여러 정보를 저장
# 연락처 추가, 삭제, 검색, 수정, 모든 연락처 보기 기능 구현.

address_book = {}

def add_address_book(name, phone, email, address):
  info = {
    f"{name}": {
      "phone": phone,
      "email": email,
      "address": address
    }
  }
  address_book.update(info)
  print("새로운 연락처 추가 완료")

def delete_address_book(target_name):
  for keyname, info in address_book.items():
    if (keyname == target_name):
      del address_book[keyname]
      print("삭제 했습니다.")
      return
  print("찾을 수 없습니다.")

def search_address_book(target_name):
  for keyname, info in address_book.items():
    if (keyname == target_name):
      print(f"이름: {keyname}, 전화번호: {info['phone']}, 이메일: {info['email']}, 주소: {info['address']}")
      return
  print("찾을 수 없습니다.")

def edit_address_book(target_name, target_info, new_info):
  for keyname, info in address_book.items():
    if target_name == keyname:
      info[target_info] = new_info
      print("수정 했습니다.")
      return
  print("찾을 수 없습니다.")

def print_all_address_book():
  for keyname, info in address_book.items():
    print("========= 모든 정보 =========")
    print(f"이름: {'keyname'}, 전화번호: {info['phone']}, 이메일: {info['email']}, 주소: {info['address']}")

