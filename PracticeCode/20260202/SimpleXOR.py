import numpy as np
import matplotlib.pyplot as plt

# 샘플 데이터 (XOR 문제)
X = np.array([
  [0, 0],
  [0, 1],
  [1, 0],
  [1, 1]])
# 입력 데이터는 2개의 특성을 가지는 4개의 샘플로 구성되어 있습니다.
# 이 데이터는 XOR 문제를 해결하기 위한 데이터입니다.
# XOR 문제는 두 개의 입력 값이 같으면 0을 출력하고, 다르면 1을 출력하는 문제입니다.
y = np.array([[0],
  [1],
  [1],
  [0]])
# 출력 데이터는 4개의 샘플에 대한 예측 값입니다.

# 시그모이드 활성화 함수
# 시그모이드 함수는 입력값을 0과 1 사이의 값으로 재현하는 활성화 함수입니다.
# 입력값을 0과 1 사이로 제한하여 비선형성 추가
def sigmoid(x):
  return 1 / (1 + np.exp(-x))
# 시그모이드 미분 함수 (역전파에서 사용)
def sigmoid_derivative(z):
  s = sigmoid(z)
  return s * (1 - s)

# 간단한 신경망 클래스
class SimpleNeuralNetwork:
  def __init__(self, input_size, hidden_size, output_size):
    # 가중치 초기화 (작은 랜덤 값)
    self.W1 = np.random.randn(input_size, hidden_size) * 0.5
    # np.random.randn : 랜덤 값 생성
    # * 0.5 : 랜덤 값을 0.5로 스케일링
    # input_size : 입력 데이터의 특성 수
    # hidden_size : 은닉층의 뉴런 수
    # 초기화된 w1의 형태는 (input_size, hidden_size)입니다.
    # input이 2개, hidden이 4개인 경우, w1의 형태는 (2, 4)입니다.
    # 0.5 곱하면 랜덤 값이 0.5 이상 0.5 이하의 값이 됩니다.
    print(f"W1 형태: {self.W1.shape}")
    self.b1 = np.zeros((1, hidden_size))
    # np.zeros : 0으로 초기화된 배열 생성
    # (1, hidden_size) : 1행 hidden_size열의 형태를 가지는 배열
    # 초기화된 b1의 형태는 (1, hidden_size)입니다.
    print(f"b1 형태: {self.b1.shape}")

    self.W2 = np.random.randn(hidden_size, output_size) * 0.5
     # np.random.randn : 랜덤 값 생성
     # * 0.5 : 랜덤 값을 0.5로 스케일링
     # hidden_size : 은닉층의 뉴런 수
     # output_size : 출력 데이터의 특성 수
     # 초기화된 W2의 형태는 (hidden_size, output_size)입니다.
    print(f"W2 형태: {self.W2.shape}")
    self.b2 = np.zeros((1, output_size))
     # np.zeros : 0으로 초기화된 배열 생성
     # (1, output_size) : 1행 output_size열의 형태를 가지는 배열
     # 초기화된 b2의 형태는 (1, output_size)입니다.
    print(f"b2 형태: {self.b2.shape}")

    # 중간 계산값 저장용 (역전파에서 사용)
    self.z1 = None # 은닉층 선형 변환 결과
    self.a1 = None # 은닉층 활성화 결과
    self.z2 = None # 출력층 선형 변환 결과
    self.a2 = None # 출력층 활성화 결과 (최종 출력)

  def forward(self, X):
    """순전파 과정"""
    print("=== 순전파 과정 ===")
    # 1단계: 입력층 -> 은닉층
    self.z1 = np.dot(X, self.W1) + self.b1 # 선형 변환
    # X는 입력 데이터이며, 입력층의 출력값입니다.
    # W1은 입력층에서 은닉층으로 가는 가중치 행렬입니다.
    # b1은 은닉층의 편향 벡터입니다.
    # z1은 은닉층의 선형 변환 결과입니다.
    # np.dot은 두 행렬의 곱을 계산하는 함수입니다.
    # 이 과정에서 입력 데이터 X와 가중치 W1이 곱해져 은닉층의 선형 변환 결과인 z1이 계산됩니다.
    print(f"1단계 - 은닉층 입력 z1 형태: {self.z1.shape}")

    self.a1 = sigmoid(self.z1) # 활성화 함수 적용
    # sigmoid 함수는 입력값을 0과 1 사이의 값으로 제한하는 활성화 함수입니다.
    # 비선형성을 부여하기 위해 시그모이드 함수를 사용합니다.
    # 이를 통해 XOR 같은 비선형 문제를 학습할 수 있는 능력을 부여합니다.
    # 은닉층의 선형 변환 결과인 z1이 sigmoid 함수에 적용되어 활성화 함수 적용 결과인 a1이 계산됩니다.
    print(f"1단계 - 은닉층 출력 a1 형태: {self.a1.shape}")

    # 2단계: 은닉층 -> 출력층
    self.z2 = np.dot(self.a1, self.W2) + self.b2 # 선형 변환
    # a1은 은닉층의 활성화 함수 적용 결과입니다.
    # W2는 은닉층에서 출력층으로 가는 가중치 행렬입니다.
    # b2는 출력층의 편향 벡터입니다.
    # z2는 출력층의 선형 변환 결과입니다.
    # np.dot은 두 행렬의 곱을 계산하는 함수입니다.
    # 이 과정에서 은닉층의 활성화 함수 적용 결과인
    # a1과 가중치 w2가 곱해져 출력층의 선형 변환 결과인 z2가 계산됩니다.
    print(f"2단계 - 출력층 입력 z2 형태: {self.z2.shape}")

    self.a2 = sigmoid(self.z2) # 최종 출력
    # z2는 출력층의 선형 변환 결과입니다.
    # sigmoid 함수는 입력값을 0과 1 사이의 값으로 제한하는 활성화 함수입니다.
    # 이 함수는 비선형성을 추가하여 모델의 표현력을 높입니다.
    # 출력층의 선형 변환 결과인 z2가 sigmoid 함수에 적용되어 최종 출력인 a2가 계산됩니다.
    print(f"2단계 - 최종 출력 a2 형태: {self.a2.shape}")
    return self.a2
  
  def backward(self, X, y, learning_rate):
    m = X.shape[0]
    # 가중치의 기울기를 평균화
    # 경사 하강법은 전체 데이터에 대한 평균 기울기를 사용하여 안정적인 학습을 진행 함
    # 구해야하는 업데이트 값
    # dL/dw1, dL/db1, dL/dw2, dL/db2
    # dL/dw2 -> dL/db2 -> dL/dw1 -> dL/db1
    # : 출력층부터 입력층으로 거꾸로 오차를 전파하는 과정
    # 마치 실수한 곳을 찾아서 책임을 거슬러 올라가는 것과 같음
    # 연쇄법칙을 위해 다음과 같이 순서대로 구해야함
    # dL/da2 -> dL/dz2 -> dL/dw2 -> dL/db2 -> dL/da1 -> dL/dz1 -> dL/dw1 -> dL/db1

    # dL/da2 구하기 (첫 번째 단계: 출력에서의 오차)
    # "우리 예측이 정답과 얼마나 다른가?"
    # self.a2 = 출력층의 활성화 함수 적용 결과 (우리의 예측값)
    # y = 실제 정답값
    #
    # L = 손실함수(np.mean((output - y)**2))의 결과
    # = 1/m * np.sum((self.a2 - y)**2)
    # 미분공식을 활용해 L의 da2에 대한 미분을 구하면, np.sum은 더해주는 역할이므로 무시
    # dL/da2 = 2/m * (self.a2 - y)
    # 2는 큰 의미가 없어 생략하고, 1/m은 dw2에서 가중치의 기울기를 평균화하기 위해 넘김
    # 즉 dL/da2 = (self.a2 - y)

    # dL/dz2 구하기 (출력층의 선형변환에서의 오차)
    # 쉬운 이해: "활성화 함수를 거치기 전 단계에서의 오차는?"
    #
    # 시그모이드 함수의 미분 공식을 활용
    # da2/dz2 = self.a2 * (1 - self.a2) # 시그모이드 함수의 미분 공식
    # 그럼 dL/dz2 = dL/da2 * da2/dz2 = (self.a2 - y) * self.a2 * (1 - self.a2)
    # 즉 dL/dz2 = (self.a2 - y) * self.a2 * (1 - self.a2)
    #
    # BCE 손실과 시그모이드 출력에서 dz2는 간단히 (출력 - 정답)으로 계산하는 것이 일반적
    # MSE에서는 적용되지 않음
    dl_dz2 = (self.a2 - y) * self.a2 * (1 - self.a2)

    # dL/dW2 구하기 (손실함수를 W2로 미분)
    # dw2는 손실 함수 L을 출력층 가중치 w2에 대해 미분한 결과 (즉, dL/dw2)
    # 쉽게 말하면: "w2를 조금 바꿨을 때 손실이 얼마나 변하는가?"
    # z2는 은닉층 출력 a1과 출력층 가중치 w2의 행렬곱으로 계산됨: z2 = np.dot(a1, W2) + b2
    # 이 식을 행렬곱 미분 규칙에 따라 w2에 대해 미분하면,
    # 각 샘플의 기여도는 a1_i (은닉층 출력), 오차는 dz2_i (z2에 대한 손실의 gradient)
    # 따라서 각 샘플의 오차 dz2_i(z2에 대한 gradient)에 대해 a1_i.T를 곱해주면
    # 해당 샘플이 w2의 변화에 얼마나 영향을 주는지 알 수 있음
    # dL/dw2 = a1_i.T @ dz2_i (i는 샘플 인덱스) (행렬곱을 통해 각 샘플의 기여도를 곱해줌)
    # 즉, dL/dw2 = np.dot(self.a1.T, dz2)
    # 그리고 손실이 평균 제곱 오차(MSE)이므로,
    # 전체 기울기를 평균 내기 위해 1/m을 곱함
    dl_dw2 = (1/m) * np.dot(self.a1.T, dl_dz2)

    # dL/db2 구하기 (손실함수를 b2로 미분)
    # db2는 손실 함수 L을 출력층 편향 b2에 대해 미분한 결과 (즉, dL/db2)
    # "편향 b2를 조금 바꿨을 때 손실이 얼마나 변하는가?"
    # z2 = np.dot(a1, W2) + b2 이므로, b2는 각 샘플에 동일하게 더해짐 (미분 공식에서 미분 결과가 1이므로)
    # 따라서 각 샘플에 대한 오차 dz2_i의 합이 편향 b2에 대한 전체 기울기가 됨
    # 즉, db2 = dz2의 모든 샘플에 대한 합 (axis=0 방향으로 합산)
    # keepdims=True는 브로드캐스팅을 위해 db2의 차원을 (1, output_size)로 유지
    # 그리고 손실 함수가 평균(MSE)이므로, 전체 샘플에 대해 평균을 내기 위해 1/m을 곱함
    dl_db2 = (1/m) * np.sum(dl_dz2, axis=0, keepdims=True)

    # dL/da1 구하기 (출력층 오차를 은닉층으로 역전파)
    # dL/da1 = dL/dz2 * dz2/da1 (연쇄법칙)
    # z2 = np.dot(a1, W2) + b2 이므로,
    # dz2/da1 = W2 (행렬곱 미분 규칙)
    # 따라서 dL/da1 = dL/dz2 * W2 = dl_dz2 @ W2.T
    # - W2.T를 곱하는 이유: 출력층 각 뉴런의 오차를 해당 가중치만큼 "역산"해서 은닉층으로 분배
    # - 마치 "출력에서 문제가 생겼는데, 이 문제에 각 은닉층 뉴런이 얼마나 기여했나?"를 계산
    # - 가중치가 클수록 해당 은닉층 뉴런의 책임도 큼
    dl_da1 = np.dot(dl_dz2, self.W2.T)

    # dL/dz1 구하기 (은닉층에서의 오차 계산)
    # 출력층의 오차가 은닉층에 어떤 영향을 주었는가?
    # dL/dz1 = dL/da1 * da1/dz1 (연쇄법칙)
    # dL/da1 = dz2 @ W2.T (출력층 오차가 가중치를 통해 역전파됨)
    # (출력층 오차가 W2를 통해 은닉층 a1으로 얼마나 영향을 주었는지를 나타냄)
    # da1/dz1 = sigmoid_derivative(z1) (시그모이드 함수의 미분)
    # 즉, dL/dz1 = dL/da1 * da1/dz1 = dz2 @ W2.T * sigmoid_derivative(z1)
    # 1/m은 가중치의 기울기를 평균화하기 위해 넘김
    dl_dz1 = dl_da1 * sigmoid_derivative(self.z1)

    # 첫 번째 은닉층 가중치와 편향의 기울기
    # 같은 패턴 반복: 입력 데이터 X와 은닉층 오차 dl_dz1을 사용해서 동일한 방식으로 구함
    dl_dw1 = (1/m) * np.dot(X.T, dl_dz1)
    dl_db1 = (1/m) * np.sum(dl_dz1, axis=0, keepdims=True)
    # 가중치 업데이트 (경사하강법)
    # 계산한 기울기(방향)를 바탕으로 가중치를 조정
    # "-=" 사용 이유: 손실을 "감소"시키는 방향으로 이동하기 위해서
    # 마치 언덕에서 아래로 내려가는 것처럼!
    # learning_rate: 얼마나 크게 조정할지 결정하는 "속도 조절기"
    self.W2 -= learning_rate * dl_dw2 # 출력층 가중치 조정
    self.b2 -= learning_rate * dl_db2 # 출력층 편향 조정
    self.W1 -= learning_rate * dl_dw1 # 은닉층 가중치 조정
    self.b1 -= learning_rate * dl_db1 # 은닉층 편향 조정
    return dl_dw1, dl_db1, dl_dw2, dl_db2
  
  def train(self, X, y, epochs, learning_rate=0.1):
    losses = []

    for epoch in range(epochs):
        # 1. 순전파
        output = self.forward(X)

        # 2. 손실 계산 (MSE)
        loss = np.mean((output - y)**2)
        losses.append(loss)

        # 3. 역전파 및 가중치 업데이트
        self.backward(X, y, learning_rate)

        if epoch % 100 == 0:
            print(f"에포크 {epoch}, 손실: {loss:.4f}")

    return losses
  
# sigmoid_derivative 함수는 시그모이드 출력값 a에 대해 도함수를 계산
nn = SimpleNeuralNetwork(2, 4, 1)
# 학습 전 예측
print("학습 전 예측:")
before_output = nn.forward(X)
print(f"예측값: {before_output.flatten()}")
print(f"정답값: {y.flatten()}")
# 학습 실행
losses = nn.train(X, y, epochs=10000, learning_rate=1.0)
# 학습 후 예측
print("\n학습 후 예측:")
after_output = nn.forward(X)
print(f"예측값: {after_output.flatten()}")
print(f"정답값: {y.flatten()}")

# 학습 곡선 시각화
plt.figure(figsize=(12, 8))
plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지
# 1. 손실 그래프
plt.subplot(2, 2, 1)
plt.plot(losses)
plt.title('학습 손실 변화')
plt.xlabel('에포크')
plt.ylabel('손실 (MSE)')
plt.grid(True)

# 2. 가중치 변화 시각화
plt.subplot(2, 2, 2)
plt.bar(range(len(nn.W1.flatten())), nn.W1.flatten())
# flatten(): 행렬을 1차원 배열로 펼침
plt.title('은닉층 가중치 (학습 후)')
plt.xlabel('가중치 인덱스')
plt.ylabel('가중치 값')

# 3. 예측 결과 비교
plt.subplot(2, 2, 3)
x_pos = np.arange(len(y))
# x_pos : 샘플의 인덱스
plt.bar(x_pos - 0.2, y.flatten(), 0.4, label='정답', alpha=0.7)
# y.flatten() : 정답 값
# 0.4 : 막대의 너비
# label : 범례
# alpha : 막대의 투명도
plt.bar(x_pos + 0.2, after_output.flatten(), 0.4, label='예측', alpha=0.7)
# x_pos + 0.2 : 예측 값의 위치
# after_output.flatten() : 예측 값
# 0.4 : 막대의 너비
# label : 범례
# alpha : 막대의 투명도

plt.title('예측 결과 비교')
plt.xlabel('샘플')
plt.ylabel('값')
plt.legend()
plt.xticks(x_pos, ['[0,0]', '[0,1]', '[1,0]', '[1,1]'])
# x_pos : 샘플의 인덱스
# ['[0,0]', '[0,1]', '[1,0]', '[1,1]'] : 샘플의 값
# 4. 신경망 구조 시각화
plt.subplot(2, 2, 4)
# 간단한 네트워크 다이어그램
plt.text(0.1, 0.7, '입력층\n(2개)', ha='center', va='center', bbox=dict(boxstyle="round", facecolor='lightblue'))
plt.text(0.5, 0.7, '은닉층\n(4개)', ha='center', va='center', bbox=dict(boxstyle="round", facecolor='lightgreen'))
plt.text(0.9, 0.7, '출력층\n(1개)', ha='center', va='center', bbox=dict(boxstyle="round", facecolor='lightcoral'))
plt.arrow(0.2, 0.7, 0.15, 0, head_width=0.05, head_length=0.02, fc='black', ec='black')
plt.arrow(0.6, 0.7, 0.15, 0, head_width=0.05, head_length=0.02, fc='black', ec='black')

# 화살표 그리기
plt.arrow(0.2, 0.7, 0.2, 0, head_width=0.02, head_length=0.02, fc='black')
plt.arrow(0.6, 0.7, 0.2, 0, head_width=0.02, head_length=0.02, fc='black')
plt.xlim(0, 1)
plt.ylim(0.5, 0.9)
plt.title('신경망 구조')
plt.axis('off')
plt.tight_layout()

# 이미지 파일로 저장
import os
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'xor_result.png')
plt.savefig(output_path, dpi=150, bbox_inches='tight')
print(f"\n시각화 결과가 저장되었습니다: {output_path}")

# plt.show()
print("\n학습 완료!")
print(f"최종 손실: {losses[-1]:.4f}")
print(f"XOR 문제 해결 정확도: {np.mean(np.abs(after_output - y) < 0.1) * 100:.1f}%")