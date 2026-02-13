import pandas as pd

# 잘못된 데이터 타입이 포함된 데이터프레임 생성
df = pd.DataFrame({
    'A': ['1', '2', '3', '4', '5'],              # 숫자이지만 문자열로 저장됨
    'B': [1.1, 2.2, 3.3, 4.4, 5.5],             # 이미 올바른 float 타입
    'C': ['2020-01-01', '2020-02-01', '2020-03-01', # 날짜이지만 문자열로 저장됨
          '2020-04-01', '2020-05-01'],
    'D': ['True', 'False', 'True', 'False', 'True'] # 불리언이지만 문자열로 저장됨
})

print("원본 데이터 타입:")
# dtypes 속성은 데이터프레임 내 각 열의 데이터 타입을 보여줍니다.
print(df.dtypes)

# 결과 분석:
# A, C, D가 모두 'object'(문자열) 타입으로 표시됨
# 이 상태로는 수치 연산, 날짜 연산, 논리 연산이 불가능함

# 1. 문자열 -> 정수 변환
# astype(int): 문자열 '1', '2' -> 정수 1, 2로 변환합니다.
df['A'] = df['A'].astype(int)
print(df['A'])
# 이제 수학적 연산(덧셈, 곱셈 등)이 가능해집니다.

# 2. 문자열 -> 날짜/시간 변환
# pd.to_datetime(): 문자열 '2020-01-01' -> datetime 객체로 변환합니다.
df['C'] = pd.to_datetime(df['C'])
print(df['C'])
# 날짜 연산(날짜 차이 계산, 월/년 추출 등)이 가능해집니다.

# 3. 문자열 -> 불리언 변환 (주의사항 있음)
df['D'] = df['D'].astype(bool)
print(df['D'])
# 주의: 문자열 'False'도 True로 변환됨 (비어있지 않은 문자열이므로)

# ================================================================
# 불리언 타입으로 변경시 모두 True가 되어버리는 문제 해결

# 원본 데이터 생성 (문자열 형태의 불리언 값들)
df_original = pd.DataFrame({
    'D': ['True', 'False', 'True', 'False', 'True']
})

# 방법 1: map() 사용
# 딕셔너리를 사용하여 특정 문자열을 실제 불리언 값으로 1:1 매칭시킵니다.
df_original['D_correct1'] = df_original['D'].map({'True': True, 'False': False})
print(df_original['D_correct1'])

# 방법 2: 조건문 사용
# 'True'라는 문자열과 같은지 비교 연산을 수행하여 그 결과를 불리언 시리즈로 만듭니다.
df_original['D_correct2'] = (df_original['D'] == 'True')
print(df_original['D_correct2'])