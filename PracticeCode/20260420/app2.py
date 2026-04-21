
import spacy

# 모델 로드
nlp = spacy.load("ko_core_news_sm")

def extract_to_api_payload(text):
    doc = nlp(text)
    
    # API 전송용 데이터 구조 (Slot 정의)
    payload = {
        "person": [],
        "location": [],
        "date": None,
        "time": None,
        "organization": [],
        "original_text": text
    }
    
    # 추출된 개체를 딕셔너리에 매핑
    for ent in doc.ents:
        if ent.label_ == "PS": # Person
            payload["person"].append(ent.text)
        elif ent.label_ == "LC": # Location
            payload["location"].append(ent.text)
        elif ent.label_ == "DT": # Date
            payload["date"] = ent.text
        elif ent.label_ == "TI": # Time
            payload["time"] = ent.text
        elif ent.label_ == "OG": # Organization
            payload["organization"].append(ent.text)
            
    return payload

# 테스트
user_input = "수강생 여러분 내일 오후 3시에 판교역에서 카카오 개발팀과 미팅 가능한가요?"
api_data = extract_to_api_payload(user_input)

import json
print("--- API 전달용 JSON 데이터 ---")
print(json.dumps(api_data, indent=4, ensure_ascii=False))

# 토큰 절약: 모든 대화 이력을 GPT에게 던지는 대신, spaCy로 핵심 정보만 추려낸 뒤 구조화된 텍스트로 전달하면 API 비용을 획기적으로 줄일 수 있습니다.
# 정확도(Grounding): GPT는 가끔 엉뚱한 소리(할루시네이션)를 합니다. 하지만 우리가 spaCy로 "장소는 서울역이야"라고 명시해 주면, GPT가 엉뚱한 장소를 말할 확률이 급격히 낮아집니다.
# 시스템 연동: 딕셔너리 형태로 정제되어 있으므로, AI 응답뿐만 아니라 실제 사내 일정 관리 DB나 Google Calendar API에 직접 데이터를 저장하기가 매우 수월합니다.