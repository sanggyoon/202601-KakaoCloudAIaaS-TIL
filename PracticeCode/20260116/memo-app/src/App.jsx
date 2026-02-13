import { useState } from 'react';
import { useEffect } from 'react';
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import MemoList from './components/MemoList';
import MemoEditor from './components/MemoEditor';
import './App.css';

function App() {
  //TODO: 메모 목록 상태를 만드세요.
  // 초기값은 id, title, content 등을 포함하는 객체 배열입니다.
  const [memos, setMemos] = useState(() => {
    const saved = localStorage.getItem('memos');
    // 힌트: 저장된 데이터가 있으면 JSON.parse()로 변환하여 반환하고, 없으면 기본 배열을 반환합니다.
    return saved
      ? JSON.parse(saved)
      : [
          {
            id: Date.now(),
            title: '메모장에 오신 것을 환영합니다!',
            content: '이것은 첫 번째 메모입니다.',
            category: '개인',
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString(),
          },
        ];
  });

  //TODO: useEffect를 사용하여 memos 상태가 변경될 때 localStorage에 저장하세요.
  useEffect(() => {
    // 힌트: localStorage.setItem('key', JSON.stringify(value));
    localStorage.setItem('memos', JSON.stringify(memos));
    // 의존성 배열에는 memos를 넣습니다.
  }, [memos]);

  //TODO: 현재 선택된 메모의 상태를 만드세요.
  // 초기값은 null 입니다.
  const [selectedMemo, setSelectedMemo] = useState(null);

  const handleNewMemo = () => {
    const newMemo = {
      id: Date.now(),
      title: '',
      content: '',
      category: '개인',
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
    };

    // 힌트: setMemos([새 메모, ...기존 메모]);
    setMemos([newMemo, ...memos]);
    // 새로 만든 메모를 바로 선택합니다.
    setSelectedMemo(newMemo);
  };

  //TODO: 메모 저장(수정) 함수를 작성하세요.
  const handleSaveMemo = (updatedMemo) => {
    // 힌트: memos 배열에서 id가 일치하는 항목을 updatedMemo로 교체합니다.
    // map() 메서드를 사용하세요.
    const newMemos = memos.map((memo) =>
      memo.id === updatedMemo.id ? updatedMemo : memo
    );
    setMemos(newMemos);
    setSelectedMemo(updatedMemo);
  };

  //TODO: 메모 삭제 함수를 작성하세요.
  const handleDeleteMemo = (memoId) => {
    // 힌트: memos 배열에서 id가 일치하지 않는 항목만 남깁니다.
    // filter() 메서드를 사용하세요.
    setMemos(memos.filter((memo) => memo.id !== memoId));
    setSelectedMemo(null);
  };

  return (
    <div className="app">
      <Header />
      <div className="main-container">
        <Sidebar />
        <MemoList
          memos={memos}
          selectedMemo={selectedMemo}
          onMemoSelect={setSelectedMemo}
          onNewMemo={handleNewMemo}
        />
        <MemoEditor
          memo={selectedMemo}
          onSave={handleSaveMemo}
          onDelete={handleDeleteMemo}
        />
      </div>
    </div>
  );
}

export default App;
