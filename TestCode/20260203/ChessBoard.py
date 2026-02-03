import numpy as np
import matplotlib.pyplot as plt

# 1. 샘플 이미지 생성 (8x8 체스보드 패턴)
sample_image = np.zeros((8, 8))

# 슬라이싱을 이용해 0과 1이 교차하도록 설정
sample_image[1::2, ::2] = 1
sample_image[::2, 1::2] = 1

# 2. sample_image 출력
plt.imshow(sample_image, cmap='gray')
plt.show()

def convolution_2d(image, kernel, stride=1, padding=0):
    """
    2D 컨볼루션 연산 구현

    Args:
        image: 입력 이미지 (H, W)
        kernel: 필터/커널 (K, K)
        stride: 이동 간격
        padding: 패딩 크기
    """
    # 입력 크기
    H, W = image.shape
    K = kernel.shape[0]
    # kernel.shape : vertical_edge 의 크기 (3)
    print(f"K: {K}")

    # 패딩 적용
    image = np.pad(image, padding, mode='constant')
    # np.pad(image, padding, mode='constant') : 이미지의 가장자리를 패딩으로 채움
    # padding : 패딩 크기
    # mode : 패딩 모드 (constant, reflect, edge, wrap)
    # constant : 0으로 채움
    # reflect : 반사 패딩
    # edge : 가장자리 복사
    # wrap : 순환 패딩
    H_padded, W_padded = image.shape

    # 출력 크기 계산
    # 원본 공식 : (H - K + 2*padding) // stride + 1
    # 이미 패딩 적용된 상태이므로 패딩 제외
    # 출력 크기 공식 : (패딩된 크기 - 커널 크기) / 스트라이드 + 1
    out_H = (H_padded - K) // stride + 1
    out_W = (W_padded - K) // stride + 1

    # 출력 배열 초기화
    output = np.zeros((out_H, out_W))
    # 초기화 하는 이유 : 컨볼루션 연산 결과를 저장할 공간을 만들기 위해

    # 컨볼루션 연산
    for i in range(out_H):
        for j in range(out_W):
            # 현재 위치
            h_start = i * stride
            # stride : 이동 간격
            h_end = h_start + K
            w_start = j * stride
            w_end = w_start + K

            # 해당 영역과 커널의 요소별 곱셈 후 합
            region = image[h_start:h_end, w_start:w_end]
            # region : 현재 위치의 영역
            # kernel : 필터/커널
            output[i, j] = np.sum(region * kernel)
            # np.sum(region * kernel) : 현재 위치의 영역과 커널의 요소별 곱셈 후 합

    return output

# 체스 보드 패턴을 가진 8x8 이미지 생성
# 흑백을 0과 255로 표현
chessboard_size = 8
chessboard = np.zeros((chessboard_size, chessboard_size), dtype=int)
for i in range(chessboard_size):
    for j in range(chessboard_size):
        if (i + j) % 2 == 0:
            chessboard[i, j] = 255 # 흰색
        else:
            chessboard[i, j] = 0 # 검은색

sample_image = chessboard # 체스 보드 이미지를 사용

vertical_edge = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
])

# 수직 에지 검출 적용
padding = (vertical_edge.shape[0] - 1) // 2
vertical_edges = convolution_2d(sample_image, vertical_edge, padding=padding)

print(f"원본 크기: {sample_image.shape}")
print(f"결과 크기: {vertical_edges.shape}")

# vertical_edges의 의미
# 수직 방향 변화가 강하게 나오는 부분은 회색으로 검출

# 결과 시각화
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(sample_image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title("Vertical Edges")
plt.imshow(vertical_edges, cmap='gray')

plt.tight_layout()
plt.show()