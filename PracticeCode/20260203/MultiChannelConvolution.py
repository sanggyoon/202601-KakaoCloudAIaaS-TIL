import numpy as np
import matplotlib.pyplot as plt

# 다중 채널 컨볼루션 (함수 정의를 먼저)
def convolution_3d(image, filters, stride=1, padding=0):
    """
    3D 컨볼루션 (다중 채널 입력, 다중 필터)
    """
    K, _, _, C_out = filters.shape
    # K : 커널의 높이
    # C_out : 커널의 출력 채널 수

    image = np.pad(image, ((padding, padding), (padding, padding), (0, 0)))
    H_padded, W_padded, C_in = image.shape

    out_H = (H_padded - K) // stride + 1
    out_W = (W_padded - K) // stride + 1
    output = np.zeros((out_H, out_W, C_out))

    for f in range(C_out):  # 각 출력 채널
        for i in range(out_H):
            for j in range(out_W):
                h_start = i * stride
                h_end = h_start + K
                w_start = j * stride
                w_end = w_start + K

                # 모든 입력 채널에서 연산 후 합
                region = image[h_start:h_end, w_start:w_end, :]
                output[i, j, f] = np.sum(region * filters[:, :, :, f])

    return output

# RGB 이미지 예시: 32x32 크기의 컬러 이미지 (3개 채널)
rgb_image = np.random.rand(32, 32, 3)

# 필터 설정: 16개의 3x3 필터 (각 필터는 입력 채널 수와 같은 3개 채널을 가짐)
filters = np.random.randn(3, 3, 3, 16)

# 첫 번째 필터의 첫 번째 채널 확인
print(f"filters : {filters[:, :, 0, 0]}")

# --- 필터의 의미 ---
# 예시 : filters[:, :, 0, 0] : 첫 번째 필터 중 빨간색(R) 채널에 대응하는 가중치 행렬
# 예시 : filters[:, :, 1, 0] : 첫 번째 필터 중 초록색(G) 채널에 대응하는 가중치 행렬
# 예시 : filters[:, :, 2, 0] : 첫 번째 필터 중 파란색(B) 채널에 대응하는 가중치 행렬

# --- 실제 응용 ---
# 총 16개의 필터가 있으므로 연산 결과 16개의 출력 채널(특징 맵)이 생성됨
# 다양한 채널의 정보를 통합하여 더 복잡하고 고차원적인 특징을 추출 가능

# 패딩 계산 및 컨볼루션 실행
padding = (filters.shape[0] - 1) // 2
feature_maps = convolution_3d(rgb_image, filters, padding=padding)
print(f"입력: {rgb_image.shape} -> 출력: {feature_maps.shape}")

# 결과
# filters : [[ 0.71455458  1.60690745  1.431584  ]
# [ 1.25201618 -1.24619664  1.06937282]
# [ 0.23047639 -2.19038809 -0.21323507]]
# 입력: (32, 32, 3) -> 출력: (32, 32, 16)

# 시각화
plt.figure(figsize=(15, 5))

# 원본 이미지
plt.subplot(1, 3, 1)
plt.title("Original RGB Image")
plt.imshow(rgb_image)

# 첫 번째 필터의 첫 번째 채널 (3x3)
plt.subplot(1, 3, 2)
plt.title("First Filter (1st channel)")
plt.imshow(filters[:, :, 0, 0], cmap='gray') # 첫 번째 필터의 첫 번째 입력 채널

# 첫 번째 특징맵
plt.subplot(1, 3, 3)
plt.title("First Feature Map")
plt.imshow(feature_maps[:, :, 0], cmap='gray')

plt.tight_layout()
import os
output_path1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'convolution_result1.png')
plt.savefig(output_path1, dpi=150, bbox_inches='tight')
print(f"저장됨: {output_path1}")
plt.show()

# 추가: 여러 필터들과 feature maps 시각화
plt.figure(figsize=(16, 8))

# 첫 번째 행: 여러 필터들 표시 (처음 4개)
for i in range(4):
    plt.subplot(2, 4, i+1)
    plt.title(f"Filter {i+1} (1st channel)")
    plt.imshow(filters[:, :, 0, i], cmap='gray')
    plt.axis('off')

# 두 번째 행: 해당 필터들의 feature maps 표시
for i in range(4):
    plt.subplot(2, 4, i+5)
    plt.title(f"Feature Map {i+1}")
    plt.imshow(feature_maps[:, :, i], cmap='gray')
    plt.axis('off')

plt.tight_layout()
output_path2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'convolution_result2.png')
plt.savefig(output_path2, dpi=150, bbox_inches='tight')
print(f"저장됨: {output_path2}")
plt.show()