import streamlit as st
from google import genai
from google.genai import types
import os
import time
import dotenv
dotenv.load_dotenv()

# ── Gemini API 설정 ──────────────────────────────────────────
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# ── Streamlit 페이지 설정 ────────────────────────────────────
st.set_page_config(
    page_title="Gemini 챗봇",
    page_icon="💬",
    layout="centered"
)

st.title("💬 Gemini 챗봇")
st.caption("Google Gemini API 기반 챗봇 서비스")

# ── 사이드바: 설정 ───────────────────────────────────────────
with st.sidebar:
    st.header("설정")

    # 모델 선택
    model_name = st.selectbox(
        "모델",
        [
            "gemini-2.5-flash",
        ],
        index=0
    )

    # 시스템 프롬프트 입력
    system_prompt = st.text_area(
        "시스템 프롬프트",
        value="당신은 친절한 AI 어시스턴트입니다. 질문에 명확하고 도움이 되는 답변을 제공하세요.",
        height=120
    )

    # 대화 초기화 버튼
    if st.button("대화 초기화", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()
    st.caption("Google AI Studio에서 API 키 발급")
    st.caption("https://aistudio.google.com/apikey")

# ── 세션 상태 초기화 ─────────────────────────────────────────
# Streamlit은 매 인터랙션마다 스크립트를 재실행하므로
# session_state로 대화 기록과 채팅 세션을 유지
if "messages" not in st.session_state:
    st.session_state.messages = []


# ── 대화 기록을 Gemini 형식으로 변환 ─────────────────────────
def build_contents():
    # session_state의 messages를 Gemini Contents 형식으로 변환
    contents = []
    for msg in st.session_state.messages:
        contents.append(types.Content(
            role="user" if msg["role"] == "user" else "model",
            parts=[types.Part(text=msg["content"])]
        ))
    return contents

# ── 대화 기록 출력 ───────────────────────────────────────────
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ── 사용자 입력 처리 ─────────────────────────────────────────
if prompt := st.chat_input("메시지를 입력하세요..."):

    # 사용자 메시지 출력 및 저장
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Gemini 응답 생성
    with st.chat_message("assistant"):
        with st.spinner("응답 생성 중..."):
            try:
                # 기존 대화 기록 + 현재 메시지를 합쳐서 전송
                contents = build_contents()
                contents.append(types.Content(
                    role="user",
                    parts=[types.Part(text=prompt)]
                ))

                for attempt in range(3):
                    try:
                        response = client.models.generate_content(
                            model=model_name,
                            contents=contents,
                            config=types.GenerateContentConfig(
                                system_instruction=system_prompt,
                                max_output_tokens=1024
                            )
                        )
                        break
                    except Exception as retry_e:
                        if "429" in str(retry_e) and attempt < 2:
                            wait = (attempt + 1) * 10
                            st.warning(f"요청 한도 초과. {wait}초 후 재시도... ({attempt+1}/3)")
                            time.sleep(wait)
                        else:
                            raise retry_e
                assistant_message = response.text

                st.markdown(assistant_message)
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": assistant_message
                })

            except Exception as e:
                error_msg = f"오류가 발생했습니다: {str(e)}"
                st.error(error_msg)
