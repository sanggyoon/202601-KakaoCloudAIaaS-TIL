import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.family'] = 'AppleGothic'                                                                                            
plt.rcParams['axes.unicode_minus'] = False    

# 기본 고객 데이터 생성
n_customers = 1000
customer_data = {
    'customer_id': range(1, n_customers + 1),
    'name': [f'Customer_{i}' for i in range(1, n_customers + 1)],
    'age': np.random.normal(35, 12, n_customers).astype(int),
    'gender': np.random.choice(['M', 'F', 'Male', 'Female', 'm', 'f', ''], n_customers),
    'city': np.random.choice(['Seoul', 'Busan', 'Daegu', 'Incheon', 'Gwangju', ''], n_customers),
    'total_purchase': np.random.exponential(50000, n_customers),
    'purchase_count': np.random.poisson(5, n_customers),
    'last_purchase_days': np.random.randint(1, 365, n_customers),
    'membership_level': np.random.choice(['Bronze', 'Silver', 'Gold', 'Platinum', ''], n_customers)
}

# 데이터프레임 생성
df_customers = pd.DataFrame(customer_data)
df_customers

# 1. 빈 문자열('')을 실제 결측치(NaN)로 변환
# 데이터 생성 시 넣었던 빈 공간들을 Pandas가 인식할 수 있는 NaN 상태로 바꿉니다.
df_customers.replace('', np.nan, inplace=True)

# 2. 성별(gender) 데이터 통일
# 'Male', 'm', 'M' -> 'M' / 'Female', 'f', 'F' -> 'F'
def clean_gender(val):
    if pd.isna(val): return val  # 결측치는 그대로 둠
    val = str(val).upper()       # 대문자로 변환
    if val in ['M', 'MALE']: return 'M'
    if val in ['F', 'FEMALE']: return 'F'
    return val

df_customers['gender'] = df_customers['gender'].apply(clean_gender)

# 3. 결측치 채우기 (Imputation)
# 성별과 도시, 등급은 가장 많이 나타나는 값(최빈값)으로 채웁니다.
df_customers['gender'] = df_customers['gender'].fillna(df_customers['gender'].mode()[0])
df_customers['city'] = df_customers['city'].fillna('Unknown') # 도시는 알 수 없음으로 처리
df_customers['membership_level'] = df_customers['membership_level'].fillna('Bronze') # 기본 등급 부여

# 4. 수치형 데이터 정제 (나이가 음수일 경우 등을 대비)
# 여기서는 0세 미만인 데이터를 평균 나이로 치환하는 예시입니다.
mean_age = df_customers['age'].mean()
df_customers.loc[df_customers['age'] < 0, 'age'] = int(mean_age)

print("--- 전처리 후 결측치 상태 ---")
print(df_customers.isnull().sum())
print("\n--- 성별 분포 확인 ---")
print(df_customers['gender'].value_counts())

# ==============================================================================================================================
# 1. VIP 기준 설정 (상위 10% 지점 계산)
threshold = df_customers['total_purchase'].quantile(0.9)

# 2. VIP 고객과 일반 고객 분리
vip_customers = df_customers[df_customers['total_purchase'] >= threshold].copy()
general_customers = df_customers[df_customers['total_purchase'] < threshold].copy()
df_customers['group'] = np.where(df_customers['total_purchase'] >= threshold, 'VIP', 'General')

# 3. 데이터 분석 - 주요 특징 비교
analysis_report = {
    '구분': ['VIP 고객', '일반 고객'],
    '인원 수': [len(vip_customers), len(general_customers)],
    '평균 연령': [vip_customers['age'].mean(), general_customers['age'].mean()],
    '평균 구매액': [vip_customers['total_purchase'].mean(), general_customers['total_purchase'].mean()],
    '평균 구매 횟수': [vip_customers['purchase_count'].mean(), general_customers['purchase_count'].mean()],
    '마지막 방문일(평균)': [vip_customers['last_purchase_days'].mean(), general_customers['last_purchase_days'].mean()]
}

# 결과 출력
report_df = pd.DataFrame(analysis_report)
print("### VIP vs 일반 고객 요약 리포트 ###")
print(report_df)

print("\n### VIP 고객이 가장 많은 도시 TOP 3 ###")
print(vip_customers['city'].value_counts().head(3))

print("\n### VIP 고객의 멤버십 등급 분포 ###")
print(vip_customers['membership_level'].value_counts())

# ==============================================================================================================================
# 시각화 테마 설정
sns.set_theme(style="whitegrid")

plt.rcParams['font.family'] = 'AppleGothic'                                                                                            
plt.rcParams['axes.unicode_minus'] = False   

# 1. 평균 구매액 비교 (막대그래프)
plt.clf()
avg_purchase = df_customers.groupby('group')['total_purchase'].mean().sort_values(ascending=False).reset_index()
sns.barplot(x='group', y='total_purchase', data=avg_purchase, hue='group', palette='viridis', legend=False)
plt.title('Average Total Purchase: VIP vs General _ 김상균')
plt.ylabel('Average Purchase Amount')
plt.xlabel('Customer Group')
plt.savefig('avg_purchase_comparison.png')

# 2. 연령 분포 비교 (히스토그램)
plt.clf()
sns.histplot(data=df_customers, x='age', hue='group', kde=True, element='step', palette='magma')
plt.title('Age Distribution: VIP vs General _ 김상균')
plt.ylabel('Frequency')
plt.xlabel('Age')
plt.savefig('age_distribution_comparison.png')

# 3. VIP 고객의 멤버십 등급 분포 (막대그래프)
plt.clf()
vip_only = df_customers[df_customers['group'] == 'VIP']
membership_counts = vip_only['membership_level'].value_counts().reset_index()
membership_counts.columns = ['level', 'count']
membership_counts = membership_counts.sort_values(by='count', ascending=False)
sns.barplot(x='level', y='count', data=membership_counts, palette='plasma')
plt.title('Membership Level Distribution (VIP Only) _ 김상균')
plt.ylabel('Number of Customers')
plt.xlabel('Membership Level')
plt.savefig('vip_membership_distribution.png')