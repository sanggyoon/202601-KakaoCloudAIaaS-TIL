import numpy as np

# 4x4 입력 데이터 생성 (풀링 연산 시연용)
input_data = np.array([
    [1,  3,  2,  4],
    [5,  6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])

print("원본 입력:")
print(input_data)
print()

def max_pooling_2d(input_array, pool_size=(2, 2), stride=2):
    """
    2D 최대 풀링 구현

    Args:
        input_array: 입력 배열 (H, W)
        pool_size: 풀링 윈도우 크기
        stride: 스트라이드

    Returns:
        풀링된 배열
    """
    h, w = input_array.shape
    pool_h, pool_w = pool_size

    # 출력 크기 계산 (패딩 없다고 가정)
    out_h = (h - pool_h) // stride + 1
    out_w = (w - pool_w) // stride + 1

    # 출력 배열 초기화
    output = np.zeros((out_h, out_w))

    # 풀링 연산 수행
    for i in range(out_h):
        for j in range(out_w):
            # 현재 윈도우 영역 계산
            h_start = i * stride
            h_end = h_start + pool_h
            w_start = j * stride
            w_end = w_start + pool_w

            # 2x2 풀링 윈도우 영역 추출
            # 2칸씩 이동하면서 최대값 선택
            # 4x4 이미지에 2x2 풀링 적용 시:
            # 첫 번째 윈도우 : 0~1행, 0~1열
            # 두 번째 윈도우 : 0~1행, 2~3열
            # 세 번째 윈도우 : 2~3행, 0~1열
            # 네 번째 윈도우 : 2~3행, 2~3열

            # 슬라이싱을 통한 윈도우 설정 및 최대값 선택
            window = input_array[h_start:h_end, w_start:w_end]
            output[i, j] = np.max(window)

    return output

def average_pooling_2d(input_array, pool_size=(2, 2), stride=2):
    """
    2D 평균 풀링 구현

    Args:
        input_array: 입력 배열 (H, W)
        pool_size: 풀링 윈도우 크기
        stride: 스트라이드

    Returns:
        풀링된 배열
    """
    h, w = input_array.shape
    pool_h, pool_w = pool_size

    # 출력 크기 계산 (패딩 없다고 가정)
    out_h = (h - pool_h) // stride + 1
    out_w = (w - pool_w) // stride + 1

    # 출력 배열 초기화
    output = np.zeros((out_h, out_w))

    # 풀링 연산 수행
    for i in range(out_h):
        for j in range(out_w):
            # 현재 윈도우 영역
            h_start = i * stride
            h_end = h_start + pool_h
            w_start = j * stride
            w_end = w_start + pool_w

            # 평균값 계산
            # 지정된 윈도우 영역([h_start:h_end, w_start:w_end]) 내의
            # 모든 원소의 산술 평균을 구하여 출력 배열에 저장합니다.
            window = input_array[h_start:h_end, w_start:w_end]
            output[i, j] = np.mean(window)

    return output

# 최대 풀링 적용
max_pooled = max_pooling_2d(input_data)
print("최대 풀링 결과:")
print(max_pooled)
print()

# 평균 풀링 적용
avg_pooled = average_pooling_2d(input_data)
print("평균 풀링 결과:")
print(avg_pooled)


import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_sample_image

# 샘플 이미지 로드
# sklearn 에서 제공하는 샘플 이미지 로드
# 이미지 크기 : 427x640x3 (높이, 너비, 채널)
image = load_sample_image("flower.jpg")

gray_image = np.mean(image, axis=2) # 그레이스케일 변환

print(f"원본 이미지 크기: {gray_image.shape}")

# 이미지에 풀링 적용
pooled_image = max_pooling_2d(gray_image, pool_size=(4, 4), stride=4)
print(f"풀링 후 이미지 크기: {pooled_image.shape}")

# 시각화
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].imshow(gray_image, cmap='gray')
axes[0].set_title(f'Original Image ({gray_image.shape})')
axes[0].axis('off')

axes[1].imshow(pooled_image, cmap='gray')
axes[1].set_title(f'4x4 Max Pooling ({pooled_image.shape})')
axes[1].axis('off')

plt.tight_layout()
plt.show()

# 크기 비교
print(f"데이터 크기 감소: {gray_image.size} -> {pooled_image.size}")
print(f"압축률: {pooled_image.size / gray_image.size:.2%}")