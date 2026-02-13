import pandas as pd
import numpy as np

# 중복 데이터가 포함된 샘플 데이터 생성
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'David', 'Bob', 'Eve', 'Charlie'],
    'Age': [25, 30, 35, 25, 40, 30, 28, 35],
    'City': ['Seoul', 'Busan', 'Seoul', 'Seoul', 'Daegu', 'Busan', 'Seoul', 'Seoul'],
    'Salary': [50000, 60000, 70000, 50000, 80000, 65000, 55000, 70000]
}

df = pd.DataFrame(data)

print("원본 데이터:")
print(df)
# len() 함수를 사용하여 전체 데이터의 행(row) 개수를 출력합니다.
print(f"\n원본 데이터 크기: {len(df)}행")

# 1. 완전 중복 행 확인
print("\n=== 완전 중복 행 탐지 ===")

# duplicated()는 모든 열의 값이 동일한 행을 찾아 True/False로 반환합니다.
duplicate_rows = df.duplicated()  # 모든 열이 동일한 행 탐지

print("중복 행 여부:")
print(duplicate_rows)

# True(1)의 합계를 구하여 중복된 행의 총 개수를 확인합니다.
print(f"완전 중복 행 개수: {duplicate_rows.sum()}개")

# 중복된 행이 하나라도 있다면 해당 행들의 내용을 출력합니다.
if duplicate_rows.sum() > 0:
    print("중복된 행들:")
    print(df[duplicate_rows])
    
# 2. 특정 열 기준 중복 확인
print("\n=== 특정 열 기준 중복 탐지 ===")

# subset 파라미터를 사용하여 'Name' 열만 기준으로 중복을 체크합니다.
# 이름이 같으면 다른 정보(급여 등)가 달라도 중복으로 간주합니다.
name_duplicates = df.duplicated(subset=['Name'])  # 이름 기준 중복
print("이름 기준 중복 행:")
print(df[name_duplicates])

# 여러 개의 열을 리스트로 전달하여 '이름'과 '나이'가 모두 같은 경우만 중복으로 체크합니다.
name_age_duplicates = df.duplicated(subset=['Name', 'Age'])  # 이름+나이 기준 중복
print("\n이름+나이 기준 중복 행:")
print(df[name_age_duplicates])

# 방법 1: 완전 중복 행 제거 (첫 번째 발생 유지)
# 모든 열의 값이 동일한 행을 찾아 삭제하며, 기본적으로 첫 번째 데이터는 남겨둡니다.
df_no_duplicates = df.drop_duplicates()
print(f"완전 중복 제거 후: {len(df_no_duplicates)}행")
# 중복된 행 중 첫번째 행만 유지
print(df_no_duplicates)

# 방법 2: 특정 열 기준 중복 제거
# subset 파라미터를 사용하여 'Name' 열이 중복되는 경우 해당 행을 삭제합니다.
df_unique_names = df.drop_duplicates(subset=['Name'])
print(f"\n이름 기준 중복 제거 후: {len(df_unique_names)}행")
# 중복된 행 중 첫번째 행만 유지
print(df_unique_names)

# 4. 조건부 중복 제거 (더 높은 급여 유지)
print("\n=== 조건부 중복 제거 (최고 급여 유지) ===")

# groupby로 이름을 묶고, 각 이름별로 'Salary'가 가장 높은 행의 인덱스(idxmax)를 추출합니다.
# 추출된 인덱스를 loc에 전달하여 해당 행들만 필터링합니다.
df_max_salary = df.loc[df.groupby('Name')['Salary'].idxmax()]

print("각 이름별 최고 급여 데이터만 유지:")
print(df_max_salary.sort_values('Name'))

# 5. 중복 데이터 통계 요약
print("\n=== 중복 데이터 요약 통계 ===")

total_rows = len(df)                                     # 전체 행 개수
unique_rows = len(df.drop_duplicates())                  # 중복 제거 후 유일한 행 개수
duplicate_count = total_rows - unique_rows               # 중복된 행의 총 개수
duplicate_percentage = (duplicate_count / total_rows) * 100 # 중복 데이터 비율(%)