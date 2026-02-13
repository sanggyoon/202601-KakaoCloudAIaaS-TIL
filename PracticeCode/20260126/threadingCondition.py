import threading
import time

# 데이터와 Condition 객체 생성
data = None
condition = threading.Condition()

# 데이터를 기다리는 스레드
def wait_for_data():
    print("대기 스레드: 데이터를 기다립니다...")

    with condition:  # Lock 획득
        condition.wait()  # 데이터가 준비될 때까지 기다림
        # 알림을 받으면 다시 Lock을 획득하고 계속 실행
        print(f"대기 스레드: 데이터 '{data}'를 받았습니다!")
        # 데이터를 준비하는 스레드
        
def prepare_data():
    global data

    print("준비 스레드: 데이터 준비 중...")
    time.sleep(2)  # 데이터 준비 시간 시뮬레이션

    with condition:  # Lock 획득
        data = "준비된 데이터"
        print("준비 스레드: 데이터가 준비되었습니다!")
        # 대기 중인 스레드 하나를 깨웁니다.
        condition.notify() 

# 스레드 생성 및 시작
# t1은 데이터를 기다리고, t2는 데이터를 준비합니다.
t1 = threading.Thread(target=wait_for_data)
t2 = threading.Thread(target=prepare_data)

t1.start()
t2.start()

# 메인 스레드는 생성된 스레드들이 종료될 때까지 기다립니다.
t1.join()
t2.join()