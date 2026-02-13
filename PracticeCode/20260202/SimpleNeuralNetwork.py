import numpy as np

def simple_neuron_chain_rule():
  """단일뉴런에서의연쇄법칙"""
  print("\n단일뉴런연쇄법칙")
  #신경망구조: x -> z -> a -> L
  # z = w*x + b (선형변환)
  # a = σ(z) (시그모이드활성화)
  # L = (a-t)² (평균제곱오차손실)

def sigmoid(z):
  return 1 / (1 + np.exp(-z))

def sigmoid_derivative(z):
  s = sigmoid(z)
  return s * (1 - s)

#실제값들
x = 1.0 #입력
w = 0.5 #가중치
b = 0.2 #편향
t = 0.8 #목표값

#순전파계산
print("순전파:")
z = w * x + b
a = sigmoid(z)
L = (a - t)**2
print(f" z = {w}*{x} + {b} = {z:.3f}")
print(f" a = σ({z:.3f}) = {a:.3f}")
print(f" L = ({a:.3f}-{t})² = {L:.3f}")

# 역전파 - 연쇄법칙으로 dL/dw 계산
print(f"\n역전파 (dL/dw 계산):")
# 손실함수 L의 가중치 w에 대한 미분
# dL_dw = dL_da * da_dz * dz_dw
# 각 단계별 미분
dL_da = 2 * (a - t) # ∂L/∂a
# 손실함수 L = (a - t)²의 a에 대한 미분:
# 거듭제곱 미분법칙 적용: d/da[(a - t)²] = 2(a - t)

da_dz = sigmoid_derivative(z) # ∂a/∂z
# 시그모이드 함수 a = σ(z) = 1/(1 + e^(-z))의 z에 대한 미분:
# σ'(z) = σ(z) * (1 - σ(z)) = a * (1 - a)
# 참고: 미분 유도 과정
# u = 1 + e^(-z), a = 1/u 라고 하면
# da/dz = da/du * du/dz = -1/u^2 * (-e^(-z))
# = e^(-z) / (1 + e^(-z))^2
# = a * (1 - a)

dz_dw = x # ∂z/∂w
# 선형변환 z = w*x + b의 w에 대한 미분:
# ∂(w*x + b)/∂w = x * 1 + 0 = x
print(f" ∂L/∂a = 2(a-t) = 2({a:.3f}-{t}) = {dL_da:.3f}")
print(f" ∂a/∂z = σ'(z) = {da_dz:.3f}")
print(f" ∂z/∂w = x = {dz_dw}")
# 연쇄법칙 적용
dL_dw = dL_da * da_dz * dz_dw
print(f"\n연쇄법칙:")
print(f" dL/dw = {dL_da:.3f} × {da_dz:.3f} × {dz_dw}")
print(f" = {dL_dw:.3f}")

# 가중치 업데이트
def simple_neuron_chain_reul():
  learning_rate = 0.1
  w_new = w - learning_rate * dL_dw
  print(f"\n가중치 업데이트:")
  print(f" w_new = w - α × ∂L/∂w")
  print(f" = {w} - {learning_rate} × {dL_dw:.3f}")
  print(f" = {w_new:.3f}")
  return w_new

new_weight = simple_neuron_chain_rule()
print(f"새로운 가중치: {new_weight}")