import csv
import time
from functools import wraps
from typing import List, Dict


# 함수 실행 시간을 측정하는 데코레이터
def measure_time(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"[{func.__name__}] 실행 시간: {execution_time:.6f}초")
        return result
    return wrapper


@measure_time
def read_csv_to_dict(filename: str) -> List[Dict]:
    
    students = []
    
    with open(filename, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # 숫자 필드는 적절한 타입으로 변환
            students.append({
                'id': int(row['id']),
                'name': row['name'],
                'age': int(row['age']),
                'score': int(row['score'])
            })
    
    return students


@measure_time
def filter_high_scorers(students: List[Dict], threshold: int = 80) -> List[Dict]:
    
    return [student for student in students if student['score'] >= threshold]


@measure_time
def calculate_average_age(students: List[Dict]) -> float:
    
    if not students:
        return 0.0
    
    total_age = sum(student['age'] for student in students)
    return total_age / len(students)


def main():

    csv_filename = 'students.csv'
    
    print("=" * 50)
    print("학생 성적 분석 프로그램")
    print("=" * 50)
    
    # 1. CSV 파일 읽기
    print("\n1. CSV 파일 읽기...")
    students = read_csv_to_dict(csv_filename)
    print(f"전체 학생 수: {len(students)}명")
    print(f"전체 학생 데이터:\n{students}")
    
    # 2. 80점 이상 학생 필터링
    print("\n2. 성적 80점 이상 학생 필터링...")
    high_scorers = filter_high_scorers(students, threshold=80)
    print(f"80점 이상 학생 수: {len(high_scorers)}명")
    for student in high_scorers:
        print(f"  - {student['name']}: {student['score']}점 (나이: {student['age']}세)")
    
    # 3. 평균 나이 계산
    print("\n3. 필터링된 학생들의 평균 나이 계산...")
    avg_age = calculate_average_age(high_scorers)
    print(f"80점 이상 학생들의 평균 나이: {avg_age:.2f}세")
    
    print("\n" + "=" * 50)
    print("분석 완료!")
    print("=" * 50)


if __name__ == "__main__":
    main()