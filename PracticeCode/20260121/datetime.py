from datetime import datetime, date, time, timedelta

# 1. 현재 날짜와 시간
# datetime.now(): 시스템의 현재 날짜와 시간을 마이크로초 단위까지 반환합니다.
now = datetime.now()
print(f"현재: {now}")

# 2. 특정 날짜/시간 생성
# 연, 월, 일, 시, 분, 초 순서대로 인자를 전달하여 객체를 만듭니다.
specific_date = datetime(2023, 12, 31, 23, 59, 59)
print(f"특정 일시: {specific_date}")

# 3. 문자열 형식 변환 (Date -> String)
# strftime (string format time): 날짜 객체를 지정한 포맷의 문자열로 바꿉니다.
date_str = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"형식화된 날짜: {date_str}")

# 4. 문자열을 날짜로 파싱 (String -> Date)
# strptime (string parse time): 문자열 데이터를 분석하여 날짜 객체로 변환합니다.
parsed_date = datetime.strptime("2023-01-15", "%Y-%m-%d")
print(f"파싱된 날짜: {parsed_date}")

# 1. 날짜 연산
# timedelta(days=1): 현재 시간에 1일을 더하여 내일 날짜를 계산합니다.
tomorrow = now + timedelta(days=1)
print(f"내일: {tomorrow}")

# timedelta(weeks=1): 현재 시간에서 1주일(7일)을 빼서 과거 날짜를 계산합니다.
last_week = now - timedelta(weeks=1)
print(f"일주일 전: {last_week}")

# 2. 날짜 비교
# 파이썬의 비교 연산자(>, <, ==)를 사용하여 날짜의 선후 관계를 판별할 수 있습니다.
if now > parsed_date:
    print("현재가 파싱된 날짜보다 이후입니다.")

# 3. 날짜와 시간 분리
# date.today(): 시간 정보 없이 오늘 날짜(연-월-일)만 가져옵니다.
today = date.today()
# time(): 특정 시점의 시, 분, 초 정보만 추출하여 별도의 객체로 만듭니다.
current_time = time(now.hour, now.minute, now.second)
print(f"오늘 날짜: {today}, 현재 시간: {current_time}")