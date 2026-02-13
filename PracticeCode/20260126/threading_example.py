# 스레드 동기화 도구
import threading
import time

# 이벤트 객체 생성
event = threading.Event()

def waiter():
    print("대기자: 이벤트를 기다리는 중...")
    # 이벤트가 설정(set)될 때까지 이 지점에서 스레드가 대기합니다.
    event.wait() 
    print("대기자: 이벤트를 수신하고 작업 진행!")

def setter():
    print("설정자: 작업 중...")
    # 특정 작업이 진행 중임을 가정하여 3초간 대기합니다.
    time.sleep(3) 
    print("설정자: 이제 이벤트를 설정합니다.")
    # 이벤트를 설정하여 wait() 상태인 다른 스레드들을 깨웁니다.
    event.set() 

# 스레드 생성 및 시작
t1 = threading.Thread(target=waiter)
t2 = threading.Thread(target=setter)

t1.start()
t2.start()