# 할 일 목록 조회
tasks = []
def view_tasks():
    if tasks:
        print("\n===== 할 일 목록 =====")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
        print("======================")
    else:
        print("할 일이 없습니다.")

def add_task(newTask):
    tasks.append(newTask)
    print(f"새로운 할 일 {newTask}이(가) 추가되었습니다.")

def complete_task(idx):
    if (0 <= idx < len(tasks)):
      tasks.remove(tasks[idx-1])
    else :
      print("존재하지 않는 일입니다.")
                                       
# 프로그램 실행 예시
add_task("파이썬 공부하기")
add_task("장보기")
add_task("운동하기")
view_tasks()
complete_task(1) # "장보기" 완료
view_tasks()