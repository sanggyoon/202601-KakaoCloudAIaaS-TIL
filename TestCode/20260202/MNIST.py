import numpy as np  # 수치 계산 라이브러리
import matplotlib.pyplot as plt  # 시각화 라이브러리
from sklearn.datasets import load_digits  # 손글씨 숫자 데이터셋 (8x8 이미지)
from sklearn.model_selection import train_test_split  # 데이터 분할 함수

class DigitClassifier:
    def __init__(self, input_size=64, hidden_size=32, output_size=10):
        # input_size=64: 입력 크기 (8x8=64 픽셀)
        # hidden_size=32: 은닉층 뉴런 수
        # output_size=10: 출력 크기 (0~9, 10개 숫자)

        # W1: 입력층→은닉층 가중치 (64x32 행렬)
        # np.random.randn: 표준정규분포에서 랜덤 값 생성
        # * 0.01: 작은 값으로 스케일링 (학습 안정성)
        self.W1 = np.random.randn(input_size, hidden_size) * 0.01

        # b1: 은닉층 편향 (1x32 행렬, 0으로 초기화)
        self.b1 = np.zeros((1, hidden_size))

        # W2: 은닉층→출력층 가중치 (32x10 행렬)
        self.W2 = np.random.randn(hidden_size, output_size) * 0.01

        # b2: 출력층 편향 (1x10 행렬, 0으로 초기화)
        self.b2 = np.zeros((1, output_size))

    def softmax(self, z):
        """Softmax 활성화 함수: 출력을 확률로 변환 (합=1)"""
        # z - np.max(z): 오버플로우 방지 (수치 안정성)
        # axis=1: 각 샘플(행)별로 최대값 계산
        # keepdims=True: 차원 유지 (브로드캐스팅용)
        exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))

        # 각 값을 전체 합으로 나눠서 확률로 변환
        # 예: [2.7, 7.4, 1.0] → [0.24, 0.67, 0.09] (합=1)
        return exp_z / np.sum(exp_z, axis=1, keepdims=True)

    def cross_entropy_loss(self, y_pred, y_true):
        """Cross-Entropy 손실 함수: 분류 문제용 손실 계산"""
        # m: 샘플 수 (y_true의 행 개수)
        m = y_true.shape[0]

        # y_true * np.log(y_pred): 정답인 클래스의 확률에 log 적용
        # + 1e-9: log(0) = -무한대 방지용 아주 작은 값
        # -np.sum(...) / m: 평균 손실 (음수를 양수로)
        loss = -np.sum(y_true * np.log(y_pred + 1e-9)) / m
        return loss

    def forward(self, X):
        """순전파: 입력 → 예측값 계산"""
        # --- 1단계: 입력층 → 은닉층 ---
        # np.dot(X, W1): 입력과 가중치 행렬 곱 (64→32)
        # + self.b1: 편향 더하기
        self.z1 = np.dot(X, self.W1) + self.b1

        # np.tanh: 활성화 함수 적용 (-1~1 사이 값)
        # 비선형성 추가로 복잡한 패턴 학습 가능
        self.a1 = np.tanh(self.z1)

        # --- 2단계: 은닉층 → 출력층 ---
        # np.dot(a1, W2): 은닉층 출력과 가중치 행렬 곱 (32→10)
        self.z2 = np.dot(self.a1, self.W2) + self.b2

        # softmax: 10개 출력을 확률로 변환
        # 예: [2.1, 0.5, ...] → [0.75, 0.05, ...] (각 숫자일 확률)
        self.a2 = self.softmax(self.z2)
        return self.a2

    def backward(self, X, y, learning_rate=0.1):
        """역전파: 오차를 이용해 가중치 업데이트"""
        # m: 샘플 수 (평균 계산용)
        m = X.shape[0]

        # === 출력층 기울기 계산 ===
        # dz2: 출력층 오차 (Softmax + Cross-Entropy 미분 결과)
        # 예측값 - 정답 (틀린 정도)
        dz2 = self.a2 - y

        # dW2: W2의 기울기 = 은닉층출력.T × 출력오차 / 샘플수
        # .T: 전치행렬 (행↔열 바꿈)
        dW2 = np.dot(self.a1.T, dz2) / m

        # db2: b2의 기울기 = 출력오차의 평균
        # axis=0: 열 방향으로 합산 (각 뉴런별)
        db2 = np.sum(dz2, axis=0, keepdims=True) / m

        # === 은닉층 기울기 계산 ===
        # da1: 은닉층으로 전파된 오차
        # 출력오차 × W2.T (가중치를 통해 역방향 전파)
        da1 = np.dot(dz2, self.W2.T)

        # dz1: tanh 미분 적용
        # tanh 미분 = 1 - tanh² (공식)
        # np.power(a1, 2): a1의 제곱
        dz1 = da1 * (1 - np.power(self.a1, 2))

        # dW1: W1의 기울기 = 입력.T × 은닉오차 / 샘플수
        dW1 = np.dot(X.T, dz1) / m

        # db1: b1의 기울기 = 은닉오차의 평균
        db1 = np.sum(dz1, axis=0, keepdims=True) / m

        # === 가중치 업데이트 (경사하강법) ===
        # 기울기의 반대 방향으로 이동 (손실 감소)
        # learning_rate: 이동 크기 (너무 크면 발산, 작으면 느림)
        self.W1 -= learning_rate * dW1  # W1 업데이트
        self.b1 -= learning_rate * db1  # b1 업데이트
        self.W2 -= learning_rate * dW2  # W2 업데이트
        self.b2 -= learning_rate * db2  # b2 업데이트

    def predict(self, X):
        """예측: 입력에 대해 숫자(0~9) 반환"""
        # forward로 확률 계산
        prob = self.forward(X)

        # np.argmax: 가장 높은 확률의 인덱스(위치) 반환
        # axis=1: 각 샘플(행)별로 최대값 위치
        # 예: [0.1, 0.7, 0.2, ...] → 1 (인덱스 1이 최대)
        return np.argmax(prob, axis=1)

    def accuracy(self, X, y):
        """정확도 계산: 맞춘 비율"""
        # 예측값 (숫자 배열)
        y_pred = self.predict(X)

        # 정답값: 원-핫 → 숫자로 변환
        # 예: [0,0,1,0,...] → 2
        y_true = np.argmax(y, axis=1)

        # y_pred == y_true: 일치 여부 (True/False 배열)
        # np.mean: True 비율 = 정확도
        # 예: [T,T,F,T,T] → 0.8 (80%)
        return np.mean(y_pred == y_true)

def mini_mnist():
    """미니 MNIST 학습 실행"""
    # === 데이터 로드 ===
    # load_digits(): sklearn 내장 손글씨 데이터셋
    digits = load_digits()

    # digits.data: 이미지 데이터 (1797개 × 64픽셀)
    # digits.target: 정답 레이블 (0~9)
    X, y = digits.data, digits.target

    # 정규화: 픽셀값 0~16 → 0~1 범위로 변환
    # 학습 안정성과 속도 향상
    X = X / 16.0

    # 원-핫 인코딩: 숫자 → 벡터 변환
    # np.eye(10): 10x10 단위행렬
    # np.eye(10)[y]: y값을 인덱스로 사용해 해당 행 선택
    # 예: 3 → [0,0,0,1,0,0,0,0,0,0]
    y_onehot = np.eye(10)[y]

    # 데이터 분할: 80% 훈련, 20% 테스트
    # random_state=42: 재현성을 위한 시드값
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_onehot, test_size=0.2, random_state=42
    )

    print("미니 MNIST 과제")
    print(f"훈련 데이터: {X_train.shape}")  # (1437, 64)
    print(f"테스트 데이터: {X_test.shape}")  # (360, 64)

    # === 모델 생성 및 학습 ===
    # 64(입력) → 32(은닉) → 10(출력) 구조
    model = DigitClassifier(input_size=64, hidden_size=32, output_size=10)

    epochs = 2000  # 전체 데이터 2000번 반복 학습

    for i in range(epochs):
        # 순전파: 예측값 계산
        model.forward(X_train)

        # 역전파: 가중치 업데이트
        model.backward(X_train, y_train, learning_rate=0.5)

        # 400번마다 진행상황 출력
        if i % 400 == 0:
            loss = model.cross_entropy_loss(model.a2, y_train)
            print(f"에포크 {i}, 손실: {loss:.4f}")

    # === 최종 평가 ===
    train_acc = model.accuracy(X_train, y_train) * 100  # 훈련 정확도
    test_acc = model.accuracy(X_test, y_test) * 100     # 테스트 정확도

    print("\n구현 후 다음을 확인하세요:")
    print(f"- 훈련 정확도: {train_acc:.1f}% (목표: 90% 이상)")
    print(f"- 테스트 정확도: {test_acc:.1f}% (목표: 85% 이상)")

# 실행
mini_mnist()