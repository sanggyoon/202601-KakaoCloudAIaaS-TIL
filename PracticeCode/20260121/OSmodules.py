# os 모듈 임포트
import os

# 1. 현재 작업 디렉토리 확인
# getcwd(): Get Current Working Directory의 약자로 현재 폴더 경로를 반환합니다.
cwd = os.getcwd()
print(f"현재 디렉토리: {cwd}")

# 2. 디렉토리 변경
# chdir('..'): 상위 디렉토리로 이동합니다.
os.chdir('../')

# 3. 디렉토리 생성 및 삭제
# mkdir: 단일 디렉토리를 생성합니다.
os.mkdir('new_folder')

# makedirs: 중첩된 디렉토리 구조를 한 번에 생성합니다.
# exist_ok=True: 이미 해당 경로가 존재해도 오류를 발생시키지 않습니다.
os.makedirs('path/to/new/folder', exist_ok=True)

# rmdir: 지정한 디렉토리를 삭제합니다.
os.rmdir('new_folder')

# 파일 및 디렉토리 목록
# os.listdir('.'): 지정한 경로(여기서는 현재 폴더 '.')에 있는 모든 파일과 폴더를 리스트로 반환합니다.
files = os.listdir('.')
print(f"현재 디렉토리 파일/폴더: {files}")

# 파일 경로 조작
# os.path.join: 운영체제별 경로 구분자(Windows는 \, Linux/Mac은 /)를 자동으로 고려하여 경로를 결합합니다.
path = os.path.join('folder', 'file.txt')  # os에 맞는 경로 구분자로 결합
dirname = os.path.dirname(path)  # 디렉토리 경로 (결과: 'folder')
basename = os.path.basename(path)  # 파일명 (결과: 'file.txt')

# 파일/디렉토리 상태 확인 (불리언 값 반환)
exists = os.path.exists(path)  # 해당 파일이나 디렉토리가 실제로 존재하는지 여부
is_file = os.path.isfile(path)  # 해당 경로가 '파일'인지 여부
is_dir = os.path.isdir(path)  # 해당 경로가 '디렉토리'인지 여부