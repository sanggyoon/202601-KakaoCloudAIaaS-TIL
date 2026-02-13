# 5개의 공개 API URL에 GET 요청을 보내고 세 가지 방식의 성능을 비교

import requests                              # 동기 HTTP 요청 라이브러리
import asyncio                               # 비동기 이벤트 루프
import aiohttp                               # 비동기 HTTP 클라이언트
import time                                  # 시간 측정용
from concurrent.futures import ThreadPoolExecutor  # 스레드 풀 관리

# 요청할 API URL 리스트 (1~5번 게시글)
API_URLS = ["https://jsonplaceholder.typicode.com/posts/1",
"https://jsonplaceholder.typicode.com/posts/2",
"https://jsonplaceholder.typicode.com/posts/3",
"https://jsonplaceholder.typicode.com/posts/4",
"https://jsonplaceholder.typicode.com/posts/5"]

# 1. 순차 처리: 하나씩 차례대로 요청 (가장 느림)
def fetch_sequential():
    return [requests.get(url).json() for url in API_URLS]

# 2. ThreadPoolExecutor: 5개 스레드로 동시 요청 (I/O 대기 시간 단축)
def fetch_threaded():
    with ThreadPoolExecutor(max_workers=5) as executor:
        # map()으로 각 URL에 요청 함수 매핑, 병렬 실행
        return list(executor.map(lambda url: requests.get(url).json(), API_URLS))

# 3. asyncio + aiohttp: 비동기로 동시 요청 (가장 효율적)
async def fetch_async():
    async with aiohttp.ClientSession() as session:  # 세션 재사용으로 효율 향상
        async def get(url):
            async with session.get(url) as resp:    # 비동기 GET 요청
                return await resp.json()            # JSON 파싱 후 반환
        # gather()로 모든 요청을 동시에 실행하고 결과 수집
        return await asyncio.gather(*[get(url) for url in API_URLS])

# 벤치마크 함수: 실행 시간 측정
def benchmark(name, func):
    start = time.perf_counter()          # 시작 시간 기록
    result = func()                       # 함수 실행
    elapsed = time.perf_counter() - start # 경과 시간 계산
    print(f"{name}: {elapsed:.3f}초, {len(result)}개 응답")

if __name__ == "__main__":
    benchmark("순차 처리", fetch_sequential)
    benchmark("ThreadPool", fetch_threaded)
    benchmark("asyncio", lambda: asyncio.run(fetch_async()))  # async 함수 실행