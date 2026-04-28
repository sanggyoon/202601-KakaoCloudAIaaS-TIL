import os
import numpy as np
from openai import OpenAI
import json
from typing import List, Dict, Optional
import dotenv
dotenv.load_dotenv()

from FAISSVectorStore import FAISSVectoreStore
from Openaiembedding import OpenAIEmbedder

class RAGPromptBuilder:
  def __init__(self):
    self.system_prompt = """
당신은 주어진 문서들을 바탕으로 정확하고 도움이 되는 답변을 제공하는 AI 어시스턴트입니다.

지침:
1. 주어진 문서 내용만을 바탕으로 답변하세요.
2. 문서에 없는 내용은 추측하지 마세요
3. 답변에 근거가 되는 문서를 명시하세요
4. 확실하지 않은 내용은 '문서에서 찾을 수 없습니다.'라고 말하세요
5. 답변은 명확하고 구체적으로 작성하세요
"""

  def build_prompt(self, query, retrieved_docs, include_sources=True):
    context = "=== 참고 문서 ===\n"
    for i, doc in enumerate(retrieved_docs, 1):
      if isinstance(doc, dict):
        doc_text = doc.get('document', doc.get('text', str(doc)))
        source = doc.get('source', f'문서 {i}')
      else:
        doc_text = str(doc)
        source = f'문서 {i}'

      context += f"\n[{source}]\n{doc_text}"

    prompt = f"""
{self.system_prompt}

{context}

=== 질문 ===
{query}

=== 답변 ===
위의 참고 문서를 바탕으로 질문에 대한 답변을 작성해주세요.
"""

    return prompt

  def build_conversational_prompt(self, query, retrieved_docs, chat_history=None):
    context = "=== 참고 문서 ===\n"
    for i, doc in enumerate(retrieved_docs, 1):
      doc_text = doc.get('document', str(doc)) if isinstance(doc, dict) else str(doc)
      context += f"\n[문서{i}]\n{doc_text}\n"

    conversation = ""
    if chat_history:
      conversation = "\n=== 이전 대화 ===\n"
      for turn in chat_history[-3:]:
        conversation += f"사용자: {turn.get('user', '')}\n"
        conversation += f"어시스턴트: {turn.get('assistant', '')}\n\n"
