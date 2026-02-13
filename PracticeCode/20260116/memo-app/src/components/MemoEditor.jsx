import { useState, useEffect } from 'react';

function MemoEditor({ memo, onSave, onDelete }) {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');

  useEffect(() => {
    if (memo) {
      setTitle(memo.title);
      setContent(memo.content);
    } else {
      setTitle('');
      setContent('');
    }
  }, [memo]);

  //TODO: 저장 버튼 클릭 시 호출될 함수를 작성하세요.
  const handleSave = () => {
    onSave({
      ...memo,
      title: title.trim(),
      content: content.trim(),
      updatedAt: new Date().toISOString(),
    });
  };

  //TODO: 삭제 버튼 클릭 시 호출될 함수를 작성하세요.
  const handleDelete = () => {
    if (window.confirm('이 메모를 삭제하시겠습니까?')) {
      onDelete(memo.id);
    }
  };

  if (!memo) {
    return (
      <div className="memo-editor no-selection">
        <p>메모를 선택하거나 새 메모를 만드세요.</p>
      </div>
    );
  }

  return (
    <div className="memo-editor">
      <div className="editor-header">
        <input
          type="text"
          className="editor-title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <div className="editor-actions">
          <button className="save-btn" onClick={handleSave}>
            저장
          </button>
          <button className="delete-btn" onClick={handleDelete}>
            삭제
          </button>
        </div>
      </div>
      <div className="editor-content">
        <textarea
          value={content}
          onChange={(e) => setContent(e.target.value)}
        />
      </div>
    </div>
  );
}

export default MemoEditor;
