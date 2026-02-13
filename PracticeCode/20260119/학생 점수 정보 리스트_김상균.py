# 학생, 점수, 정보, 리스트, 이름
# 학생들의 이름과 점수 정보를 리스트로 관리하는 코드 구현
# 다음 기능을 구현하세요:
  # 학생 추가: 이름과 점수를 입력 받아 목록에 추가
  # 학생 삭제: 이름을 입력 받아 해당 학생 정보 삭제
  # 성적 수정: 이름을 입력 받아 해당 학생의 점수 수정
  # 전체 목록 출력: 모든 학생의 이름과 점수 출력
  # 통계 출력: 최고 점수, 최저 점수, 평균 점수 계산 및 출력

class Student:
  def __init__(self, name, score) :
    self.name = name
    self.score = score

  def editScore(self, newScore) :
    self.score = newScore

students = []

def print_all_students() :
  print("=== 전체 학생 목록 ===")

  if len(students) == 0 :
    print("학생이 없습니다.")
    return
  
  for i, student in enumerate(students) :
    print(f"{i+1}번 학생: {student.name} - {student.score}점")

def add_student (name, score) :
  students.append(Student(name, score))
  print(f"{name} 학생 추가")

def delete_student (name) :
  for student in students :
    if student.name == name :
      students.remove(student)
      print(f"{name} 학생 삭제")
      return
  print("학생을 찾을 수 없습니다.")

def edit_student_score (name, score) :
  for student in students :
    if student.name == name :
      student.editScore(score)
      print(f"{name} 학생 점수 {score}점으로 수정 완료")
      return
  print("학생을 찾을 수 없습니다.")

def print_statistics() :
  highScore = 0
  lowScore = 100
  avgScore = 0

  if len(students) == 0 :
    print("학생이 없습니다.")
    return
  
  for i, student in enumerate(students) : 
    if (highScore < student.score) :
      highScore = student.score
    if (lowScore > student.score) :
      lowScore = student.score
    avgScore += student.score

  avgScore /= len(students)

  print(f"최고 점수: {highScore} | 최저 점수: {lowScore} | 평균 점수: {avgScore:.1f}")

# 테스트 코드
add_student("홍길동", 30)
add_student("전우치", 60)

print_all_students()
print_statistics()

edit_student_score("홍길동", 70)
edit_student_score("각시탈", 100)

print_all_students()
print_statistics()

delete_student("홍길동")

print_all_students()
print_statistics()

delete_student("전우치")

print_all_students()
print_statistics()
