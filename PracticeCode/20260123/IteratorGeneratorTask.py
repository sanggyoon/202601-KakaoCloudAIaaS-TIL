log_data = """2023-11-20 10:15:32 INFO: 사용자 로그인 성공
2023-11-20 10:16:45 ERROR: 데이터베이스 연결 실패
2023-11-20 10:17:23 WARNING: 비정상적인 접근 시도
2023-11-20 10:18:01 INFO: 세션 갱신 완료
2023-11-20 10:20:14 INFO: 사용자 로그아웃
2023-11-20 10:25:43 WARNING: 디스크 사용량 80% 초과
2023-11-20 10:30:12 INFO: 백업 작업 시작
2023-11-20 10:31:55 INFO: 백업 작업 완료
2023-11-20 10:45:07 ERROR: 캐시 서버 응답 없음
2023-11-20 10:50:33 INFO: 서비스 재시작 시도
2023-11-20 10:52:10 INFO: 서비스 재시작 완료
2023-11-20 11:05:11 ERROR: 메모리 부족 오류
2023-11-20 11:06:45 WARNING: 메모리 사용량 90% 초과
2023-11-20 11:08:22 INFO: 가비지 컬렉션 수행
2023-11-20 11:10:55 INFO: 시스템 상태 정상
2023-11-20 11:20:03 ERROR: 외부 API 호출 실패
2023-11-20 11:25:19 INFO: 외부 API 재시도 성공
2023-11-20 11:40:41 WARNING: 네트워크 지연 감지
2023-11-20 11:45:30 INFO: 네트워크 상태 복구
2023-11-20 12:00:00 INFO: 정기 점검 시작
2023-11-20 12:30:00 INFO: 정기 점검 종료"""

def log_reader(logs):
  for line in logs.strip().split('\n'):
    yield line

def error_filter(log_stream, state):
  for line in log_stream:
    if state in line:
      yield line

print("\n======= 전체 로그 출력 =======")
raw_logs = log_reader(log_data)
for error in raw_logs:
  print(error)

states = ["ERROR", "WARNING", "INFO"]
for state in states:
  raw_logs = log_reader(log_data)
  errors_only = error_filter(raw_logs, state)
  print(f"\n======= {state} 필터링된 로그 출력 =======")
  for error in errors_only:
    print(error)
