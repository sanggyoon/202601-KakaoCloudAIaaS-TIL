// ms(밀리초)만큼 기다렸다가 resolve되는 Promise를 반환하는 유틸 함수
// async/await에서 시간 지연을 만들기 위한 표준 패턴
const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

// 페이지 단위로 데이터를 가져오는 paginator를 생성하는 함수
// fetchPage는 (page) => { data: [], hasMore: boolean } 형태의 async 함수
function createPaginator(fetchPage) {
  // async iterable 객체를 반환
  // 이 객체는 for await...of로 순회 가능
  return {
    // Symbol.asyncIterator를 구현한 async generator 메서드
    // for await...of가 이 메서드를 호출하여 iterator를 얻음
    async *[Symbol.asyncIterator]() {
      // 현재 페이지 번호
      // generator 실행 컨텍스트 내부 상태로 유지됨
      let page = 1;

      // 종료 조건을 내부에서 직접 제어하기 위해 무한 루프 사용
      while (true) {
        // 현재 페이지 번호로 비동기 데이터 요청
        // fetchPage가 Promise를 반환하므로 await 필요
        const { data, hasMore } = await fetchPage(page);

        // 현재 페이지의 data를 외부로 전달
        // 이 시점에서 generator 실행은 "중단"됨
        yield data;

        // 더 가져올 페이지가 없다면
        if (!hasMore) {
          // generator 종료
          // for await...of는 done === true를 받고 반복을 멈춤
          return;
        }

        // 다음 페이지로 이동
        page += 1;
      }
    },
  };
}

// -------------------- 테스트 코드 --------------------

// page 번호를 받아 mock 데이터를 반환하는 비동기 함수
const mockFetch = async (page) => {
  // 네트워크 요청을 흉내 내기 위해 100ms 지연
  await delay(100);

  // 페이지별 데이터와 다음 페이지 존재 여부 반환
  return {
    // 현재 페이지 번호를 문자열에 포함한 테스트 데이터
    data: [`item-${page}-1`, `item-${page}-2`],

    // page가 3보다 작을 때만 다음 페이지 존재
    hasMore: page < 3,
  };
};

// mockFetch를 사용해 paginator 생성
const paginator = createPaginator(mockFetch);

// paginator는 async iterable이므로 for await...of로 순회 가능
for await (const items of paginator) {
  // 각 반복마다 yield된 data 배열이 items로 들어옴
  console.log(items);
}

// 실제 출력 결과
// ['item-1-1', 'item-1-2']
// ['item-2-1', 'item-2-2']
// ['item-3-1', 'item-3-2']
