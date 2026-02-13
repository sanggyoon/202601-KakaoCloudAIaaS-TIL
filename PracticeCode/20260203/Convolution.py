import numpy as np

def full_convolution_demo():
    """전체 컨볼루션 과정 시연"""

    # 5x5 입력 이미지 (위에서 아래로 밝아지는 패턴)
    image = np.array([
        [50,  50,  50,  50,  50],  # 밝은 영역
        [50,  50,  50,  50,  50],  # 밝은 영역
        [100, 100, 100, 100, 100],  # 중간 영역
        [150, 150, 150, 150, 150],  # 어두운 영역
        [150, 150, 150, 150, 150]   # 어두운 영역
    ])

    # 수평 에지 검출 필터 (Horizontal Edge Detection Filter)
    filter = np.array([
        [-1, -1, -1],
        [ 0,  0,  0],
        [ 1,  1,  1]
    ])

    # 3x3 출력 배열 (특징 맵) 초기화
    output = np.zeros((3, 3))

    print("각 위치별 컨볼루션 계산:")
    for i in range(3):
        for j in range(3):
            # 현재 3x3 영역 추출
            region = image[i:i+3, j:j+3]
            # 3x3 영역 출력
            print(f"현재 영역: {region}")

            # 컨볼루션 계산
            result = np.sum(region * filter)
            output[i, j] = result

            print(f"위치 ({i},{j}): {result}")

            
    print(f"\n최종 출력:\n{output}")
    print("\n해석:")
    print("- 0에 가까운 값: 에지 없음")
    print("- 큰 음수/양수: 강한 에지 검출")

full_convolution_demo()