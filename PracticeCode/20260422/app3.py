from openai import OpenAI
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os
from dotenv import load_dotenv
load_dotenv()

class OpenAIEmbedder:
  def __init__(self, api_key):
    self.client = OpenAI(api_key = api_key)
    self.model = "text-embbedding-3-small"

  def get_embedding(self, text):
    try:
      response = self.client.embeddings.create(
        model = self.model,
        input = text
      )
      return response.data[0].embedding
  
    except Exception as e:
      print(f"임베딩 오류: {e}")
      return None
    
  def get_batch_embeddings(self, texts):
    try:
      response = self.client.embeddings.create(
        model = self.model,
        input = texts
      )
      return [data.embedding for data in response.data]
    
    except Exception as e:
      print(f"배치 임베딩 오류: {e}")
      return []
    
embedder = OpenAIEmbedder(os.getenv("OPENAI_API_KEY"))
embedding = embedder.get_embedding("안녕하세요")
print(f"임베딩 차원: {len(embedding) if embedding else 0}")

if embedding:
  print(f"임베딩 벡터 (처음 10개 값): {embedding[:10]})")

  similarity = cosine_similarity([embedding], [embedding])
  print(f"유사도: {similarity[0][0]}")
else:
  print("임베딩  생성에 실패했습니다.")