def fixed_size_chunking(text, chunk_size=500, overlap=0):
  """
  고정 크기로 텍스트를 청킹하는 함수
  """

  chunks = []
  start = 0

  while start < len(text):
    end = start + chunk_size
    chunk = text[start:end]
    chunks.append(chunk)
    start = end - overlap

  return chunks

sample_text = """
Porro dolore eius est. Non quaerat neque dolorem. Etincidunt etincidunt est quisquam voluptatem sit. Quaerat modi non modi dolor tempora consectetur non. Ipsum consectetur quisquam ipsum amet ut velit. Velit tempora aliquam non numquam aliquam magnam.

Porro labore modi velit. Adipisci sed dolor ut dolorem. Ipsum dolore quiquia adipisci velit sit. Dolor ut ipsum dolorem labore. Aliquam ut consectetur neque consectetur quisquam ipsum non. Aliquam eius eius amet porro adipisci porro etincidunt.

Amet voluptatem consectetur velit amet. Labore labore est quisquam. Eius amet etincidunt numquam amet porro aliquam. Tempora tempora eius magnam neque. Modi numquam est dolor eius quaerat dolorem magnam.

Adipisci numquam quaerat labore numquam sit neque quisquam. Sed consectetur consectetur quiquia etincidunt labore dolor sed. Consectetur non dolor dolorem aliquam eius. Non dolorem neque porro velit porro dolorem. Non dolorem labore ipsum modi ut est.
"""

chunks = fixed_size_chunking(sample_text, chunk_size=100, overlap=0)
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {chunk}")
    print("-" * 50)