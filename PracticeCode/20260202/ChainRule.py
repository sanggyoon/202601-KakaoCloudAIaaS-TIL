import numpy as np
import matplotlib.pyplot as plt

def travel_chain_rule_example():
  print("자동차 여행 연쇄법칙")

# 함수 정의
def distance_to_time(distance):
  """거리(km) -> 시간(hour)"""
  speed = 80 # km/h
  return distance / speed

def time_to_cost(time):
  """시간(hour) -> 비용(원)"""
  hourly_cost = 10000 # 시간당 1만원
  return time * hourly_cost

# 현재 상황
distance = 400 # km (서울-부산)
time = distance_to_time(distance) # 5시간
cost = time_to_cost(time) # 50,000원
print(f"거리: {distance}km")
print(f"시간: {time}시간")
print(f"비용: {cost:,}원")

# 수학적 계산
d_cost_d_time = 10000 # ∂(비용)/∂(시간)
d_time_d_distance = 1/80 # ∂(시간)/∂(거리)
# 연쇄법칙 적용: ∂(비용)/∂(거리)
# = ∂(비용)/∂(시간) × ∂(시간)/∂(거리)
d_cost_d_distance = d_cost_d_time * d_time_d_distance
print(f"∂(비용)/∂(시간) = {d_cost_d_time}원/시간")
print(f"∂(시간)/∂(거리) = {d_time_d_distance:.4f}시간/km")
print(f"∂(비용)/∂(거리) = {d_cost_d_distance:.0f}원/km")
# 결론: 거리 1km 증가 -> 비용 125원 증가

def basic_chain_rule_math():
  """기본 수학 연쇄법칙"""
  print("\n수학적 연쇄법칙 기초")
  # 예제 1: f(g(x))의 미분
  print("예제 1: y = (2x + 1)³ 의 미분")
  # 함수 분해
  print("함수 분해:")
  print(" u = 2x + 1 (안쪽 함수)")
  print(" y = u³ (바깥쪽 함수)")