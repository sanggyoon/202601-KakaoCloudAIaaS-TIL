import pandas as pd
import numpy as np

# 결측치가 있는 데이터프레임 생성
# np.nan을 사용하여 데이터가 없는 빈 칸(결측치)을 인위적으로 만듭니다.
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, 5],
    'C': [1, 2, 3, np.nan, np.nan]
})

print("원본 데이터:")
print(df)

# 결측치 확인
# isna()는 각 요소가 결측치(NaN)인지 확인하여 True(결측치) 또는 False를 반환합니다.
print("\n결측치 여부:")
print(df.isna())

# 결측치 개수 확인
print("\n열별 결측치 개수:")
# isna()로 찾은 결측치(True)들을 sum()으로 더해 각 열의 결측치 총합을 구합니다.
print(df.isna().sum())

# 결측치 처리 방법 1: 삭제
# dropna()는 결측치가 하나라도 포함된 행(row)을 전체 데이터셋에서 삭제합니다.
df_dropped = df.dropna()  # 결측치가 있는 행 모두 삭제

print("\n결측치 행 삭제 후:")
print(df_dropped)

# 결측치 처리 방법 2: 채우기
# fillna(값)는 데이터프레임 내의 모든 NaN을 지정한 값으로 바꿉니다.
df_filled = df.fillna(0)  # 결측치를 0으로 채우기
print("\n결측치를 0으로 채운 후:")
print(df_filled)

# 결측치 처리 방법 3: 열별 평균으로 채우기
# df.mean()을 인자로 주면 각 열의 산술 평균값을 계산하여 해당 열의 빈칸을 채웁니다.
df_mean = df.fillna(df.mean())  # 각 열의 평균값으로 채우기
print("\n결측치를 평균으로 채운 후:")
print(df_mean)