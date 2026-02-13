import threading
import queue
import time
import random

# 작업 큐 생성
task_queue = queue.Queue()
# 결과 큐 생성
result_queue = queue.Queue()

# 작업 생성 함수 (Producer 역할)
def create_tasks():
    print("작업 생성 시작")
    
    # 10개의 작업 생성
    for i in range(10):
        task = f"작업-{i}"
        task_queue.put(task)  # 작업 보관함(큐)에 넣음
        print(f"작업 추가: {task}")
        # 0.1~0.3초 사이의 랜덤한 간격을 두고 작업 생성
        time.sleep(random.uniform(0.1, 0.3))
        
    # 영업 종료 신호 (워커 수만큼 추가)
    # 'None'을 넣어 워커 스레드에게 더 이상 작업이 없음을 알립니다.
    for _ in range(3):  # 워커(요리사)가 3명임을 가정
        task_queue.put(None)  # None은 "오늘 장사 끝" 신호
        
    print("모든 작업 생성 완료")

    # 작업 처리 함수
def worker(worker_id):
    print(f"워커 {worker_id} 시작")  # 출근 신고
    while True:  # 계속 일하는 무한 루프
        # 작업 가져오기 (주문서 확인)
        task = task_queue.get()  # 보관함에서 작업 꺼냄
        
        # 퇴근 시간인지 확인
        if task is None:  # "오늘 장사 끝" 신호 확인
            print(f"워커 {worker_id} 종료")  # 퇴근!
            break  # 무한 루프 종료
            
        # 작업 처리 (요리 만들기)
        print(f"워커 {worker_id}가 {task} 처리 중...")
        processing_time = random.uniform(0.5, 1.5)  # 요리 시간은 랜덤
        time.sleep(processing_time)  # 요리하는 시간
        
        # 결과 제출 (완성된 요리 올려두기)
        result = f"{task} 완료 (소요시간: {processing_time:.2f}초)"
        result_queue.put((worker_id, result))  # 결과 보관함에 넣음
        
        # 작업 완료 표시 (주문서에 완료 도장)
        # 현재 처리 중인 특정 작업 하나가 완료되었음을 큐에 알립니다.
        task_queue.task_done()
        print(f"남은 작업 수: {task_queue.qsize()}")

        # 결과 수집 함수
def result_collector():
    print("결과 수집기 시작")  # 서빙 직원 출근
    results = []  # 완료된 주문 기록용

    # 총 10개 결과 수집 (10개 요리 서빙)
    for _ in range(10):
        # 결과 큐에서 워커 ID와 결과 메시지를 꺼내옵니다.
        worker_id, result = result_queue.get()  # 완성된 요리 가져오기
        print(f"결과 수신: 워커 {worker_id} -> {result}")
        
        # 리스트에 결과를 추가하여 기록을 남깁니다.
        results.append(result)  # 결과 기록
        
        # 해당 결과 처리가 완전히 끝났음을 큐에 알립니다.
        result_queue.task_done()  # "이 요리 서빙했어요" 표시

    print(f"총 {len(results)}개 결과 수집 완료")  # 서빙 완료

    # 스레드 생성 및 시작
# 1. 작업을 만드는 생산자 스레드 생성
creator = threading.Thread(target=create_tasks)

# 2. 작업을 처리하는 워커 스레드들 생성 (3명의 워커)
workers = [threading.Thread(target=worker, args=(i,)) for i in range(3)]

# 3. 결과를 수집하는 컬렉터 스레드 생성
collector = threading.Thread(target=result_collector)

# 스레드 시작
creator.start()
for w in workers:
    w.start()
collector.start()

# 스레드 종료 대기
# 메인 스레드가 각 스레드의 작업이 끝날 때까지 기다립니다.
creator.join()
for w in workers:
    w.join()
collector.join()

print("모든 작업 완료!")  # 오늘 영업 끝!