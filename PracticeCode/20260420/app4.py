import anthropic
import os
import dotenv
dotenv.load_dotenv()

class ClaudeChatbot:
    def __init__(self, api_key: str, model: str = "claude-sonnet-4-6"):
        # Anthropic 클라이언트 생성
        self.client = anthropic.Anthropic(api_key=api_key)
        # 사용할 Claude 모델 설정
        self.model = model
        # 대화 기록 (user/assistant 메시지만 저장 — system은 별도 관리)
        self.conversation_history = []
        # 시스템 프롬프트 — Claude API는 system을 messages 밖에서 별도로 전달
        self.system_message = "당신은 카페 주문을 받는 친절한 직원입니다. 메뉴 추천과 주문 처리를 도와주세요."

    def add_message(self, role: str, content: str):
        """대화 히스토리에 메시지 추가"""
        # role: "user" 또는 "assistant"
        self.conversation_history.append({
            "role": role,
            "content": content
        })

    def get_response(self, user_message: str) -> str:
        """사용자 메시지에 대한 응답 생성"""
        self.add_message("user", user_message)

        try:
            # Claude Messages API 호출
            # OpenAI와 다르게 system은 별도 파라미터로 전달
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                system=self.system_message,        # 시스템 프롬프트 (별도 파라미터)
                messages=self.conversation_history  # user/assistant 대화 기록
            )

            # 응답 텍스트 추출
            # response.content는 리스트 — 첫 번째 TextBlock의 text 사용
            assistant_message = response.content[0].text

            # 응답을 대화 기록에 추가 (맥락 유지)
            self.add_message("assistant", assistant_message)

            return assistant_message

        except Exception as e:
            return f"오류가 발생했습니다: {str(e)}"


# API 키 환경변수에서 로드
api_key = os.environ.get("ANTHROPIC_API_KEY")

# 챗봇 인스턴스 생성
chatbot = ClaudeChatbot(api_key)

# 대화 시작
user_input = "안녕하세요, 추천 메뉴가 있나요?"
response = chatbot.get_response(user_input)
print(f"챗봇: {response}")

# 연속 대화 — 이전 맥락 유지
user_input = "달지 않은 음료를 원해요"
response = chatbot.get_response(user_input)
print(f"챗봇: {response}")

# 대화 루프
while True:
    user_input = input("나: ")
    if user_input == "종료":
        break
    response = chatbot.get_response(user_input)
    print(f"챗봇: {response}")
