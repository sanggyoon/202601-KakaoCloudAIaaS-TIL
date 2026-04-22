from openai import OpenAI
import os
import dotenv
dotenv.load_dotenv()

class OpenAIChatbot:
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        """
        OpenAI 챗봇 초기화
        """
        # OpenAI 클라이언트 생성
        self.client = OpenAI(api_key=api_key)
        # 사용할 OpenAI 모델 설정 (기본값: gpt-3.5-turbo)
        self.model = model
        # 대화 기록을 저장하는 리스트 - 각 메시지는 딕셔너리 형태로 저장
        self.conversation_history = []
        # 시스템 메시지 - AI의 역할과 행동 방식을 정의하는 기본 프롬프트
        self.system_message = {
            "role": "system",  # 메시지 역할: system, user, assistant 중 하나
            "content": "당신은 까페 주문을 받는 친절한 직원입니다. 메뉴 추천과 주문 처리를 도와주세요."
        }

    def add_message(self, role: str, content: str):
        """대화 히스토리에 메시지 추가"""
        # 새로운 메시지를 대화 기록에 추가
        # role: "user" 또는 "assistant" - 메시지를 보낸 주체를 나타냄
        # content: 실제 메시지 내용
        self.conversation_history.append({
            "role": role,
            "content": content
        })
        # 이 함수는 대화의 맥락을 유지하기 위해 모든 메시지를 기록함

    def get_response(self, user_message: str) -> str:
        """사용자 메시지에 대한 응답 생성"""
        # 사용자 메시지를 대화 기록에 먼저 추가
        self.add_message("user", user_message)

        # 시스템 메시지와 대화 히스토리를 결합하여 전체 컨텍스트 구성
        # OpenAI API는 전체 대화 맥락을 필요로 함
        messages = [self.system_message] + self.conversation_history

        try:
            # OpenAI Chat Completions API 호출
            response = self.client.chat.completions.create(
                model=self.model,  # 사용할 AI 모델
                messages=messages,  # 전체 대화 맥락
                max_tokens=1000,  # 생성할 최대 토큰 수 (응답 길이 제한)
                temperature=0.7,  # 창의성 조절 (0.0~2.0, 높을수록 창의적/무작위적)
                presence_penalty=0.6,  # 새로운 주제 언급 촉진 (반복 억제)
                frequency_penalty=0.0  # 단어/구문 반복 억제 (0.0~2.0), 0.0은 억제하지 않음
            )

            # 응답 생성
            # API 응답에서 실제 메시지 내용 추출
            assistant_message = response.choices.message.content
            # response.choices.message.content : 첫 번째 선택지의 메시지 내용
            # 일반적인 셋팅에서는 첫번째 응답이 AI가 판단한 최적의 응답

            # 어시스턴트의 응답을 대화 기록에 추가 (맥락 유지를 위함)
            self.add_message("assistant", assistant_message)

            return assistant_message

        except Exception as e:
            # API 호출 실패 시 오류 메시지 반환
            # 네트워크 오류, API 키 문제, 할당량 초과 등의 상황에서 발생
            return f"오류가 발생했습니다: {str(e)}"
        
    def clear_history(self):
        """대화 히스토리 초기화"""
        # 대화 기록을 완전히 삭제
        # 새로운 대화를 시작하거나 메모리 사용량을 줄일 때 사용
        self.conversation_history = []
        # 시스템 메시지는 유지되어 AI의 기본 역할은 계속 적용됨

    def set_system_prompt(self, prompt: str):
        """시스템 프롬프트 설정"""
        # AI의 역할과 행동 방식을 새로 정의
        # prompt: AI가 어떻게 행동해야 하는지를 설명하는 지시문
        self.system_message["content"] = prompt
        # 예: "당신은 요리 전문가입니다", "당신은 친절한 상담사입니다" 등