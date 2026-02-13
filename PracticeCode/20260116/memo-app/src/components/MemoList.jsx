function MemoList({ memos, selectedMemo, onMemoSelect, onNewMemo }) {
  return (
    <div className="memo-list">
      <div className="memo-list-header">
        <h2>메모 ({memos.length})</h2>
        <button className="new-memo-btn" onClick={onNewMemo}>
          + 새 메모
        </button>
      </div>

      <div className="memo-items">
        {/*TODO: memos 배열을 map()을 사용하여 렌더링하세요. */}
        {memos.map((memo) => (
          <div
            key={memo.id}
            className={`memo-item ${
              selectedMemo?.id === memo.id ? 'active' : ''
            }`}
            onClick={() => onMemoSelect(memo)}
          >
            <div className="memo-item-title">{memo.title || '제목 없음'}</div>
            <div className="memo-item-preview">
              {memo.content || '내용 없음'}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default MemoList;
