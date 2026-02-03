import numpy as np

# 원본 3x3 이미지 (간단한 예시)
original = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("원본 이미지 (3x3):")
print(original)

# 1. Zero Padding (가장 일반적)
zero_padded = np.pad(original, pad_width=1, mode='constant', constant_values=0)
print("Zero Padding (pad=1):")
print(zero_padded)
print("-> 가장자리를 0으로 채움 (기본값)")

# 2. Reflect Padding (대칭 반사)
reflect_padded = np.pad(original, pad_width=1, mode='reflect')
print("Reflect Padding (pad=1):")
print(reflect_padded)
print("-> 가장자리를 기준으로 대칭 반사")

# 3. Edge Padding (가장자리 복사)
edge_padded = np.pad(original, pad_width=1, mode='edge')
print("Edge Padding (pad=1):")
print(edge_padded)
print("-> 가장자리 픽셀 값을 복사 (1,1,1... / 3,3,3...)")

# 4. Wrap Padding (순환)
wrap_padded = np.pad(original, pad_width=1, mode='wrap')
print("Wrap Padding (pad=1):")
print(wrap_padded)
print("-> 반대편에서 값을 가져옴 (마치 이미지가 연결된 것처럼)")

# 시각적 비교 요약
print("패딩 효과 요약:")
print("Zero    : 경계가 명확, 인위적 경계 생성")
print("Reflect : 자연스러운 전환, 에지 보존")
print("Edge    : 부드러운 전환, 경계 흐림")
print("Wrap    : 주기적 패턴에 적합")

print("출력 크기 계산 예시")
print("입력 | 필터 | 스트라이드 | 패딩 | 출력")
# 출력 크기 공식
def calculate_output_size(input_size, kernel_size, stride, padding):
    """출력 크기 계산"""
    return (input_size - kernel_size + 2*padding) // stride + 1

# 다양한 조합 테스트
examples = [
    {"input": 224, "kernel": 7, "stride": 2, "padding": 3},
    {"input": 32,  "kernel": 3, "stride": 1, "padding": 1},
    {"input": 28,  "kernel": 5, "stride": 1, "padding": 0},
    {"input": 56,  "kernel": 3, "stride": 2, "padding": 1}
]

for ex in examples:
    output = calculate_output_size(ex["input"], ex["kernel"],
                                 ex["stride"], ex["padding"])
    print(f"{ex['input']:3d} | {ex['kernel']:2d} | {ex['stride']:6d} | {ex['padding']:2d} | {output:3d}")

calculate_output_size