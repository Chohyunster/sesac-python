# coding=utf8
# REST API 호출에 필요한 라이브러리
import requests
import json
from dotenv import load_dotenv
import os

# [내 애플리케이션] > [앱 키] 에서 확인한 REST API 키 값 입력
# REST_API_KEY = '${REST_API_KEY}'
# 위 두줄처럼 하드코딩 안 하고 env파일에서 가져오기
load_dotenv()
REST_API_KEY = os.getenv('KAKAO_API_KEY')

# KoGPT API 호출을 위한 메서드 선언
# 각 파라미터 기본값으로 설정
def kogpt_api(prompt, max_tokens = 1, temperature = 1.0, top_p = 1.0, n = 1):
    r = requests.post(
        'https://api.kakaobrain.com/v1/inference/kogpt/generation',
        json = {
            'prompt': prompt,
            'max_tokens': max_tokens,
            'temperature': temperature,
            'top_p': top_p,
            'n': n
        },
        headers = {
            'Authorization': 'KakaoAK ' + REST_API_KEY,
            'Content-Type': 'application/json'
        }
    )
    # 응답 JSON 형식으로 변환
    response = json.loads(r.content)
    return response

# KoGPT에게 전달할 명령어 구성
# prompt = '''인간처럼 생각하고, 행동하는 '지능'을 통해 인류가 이제까지 풀지 못했던'''

# 파라미터를 전달해 kogpt_api()메서드 호출
# response = kogpt_api(
#     prompt = prompt,
#     max_tokens = 48,   #token은 글자수가 아니라 내부적으로 처리할 때의 단위이다.
#     temperature = 1.0,
#     top_p = 1.0,
#     n = 3
# )

# # print(response)
# print(response['generations'][0]['text'])
# print(response['generations'][1]['text'])
# print(response['generations'][2]['text'])

# print('=' * 50)

#3. 문장 분류하기
# prompt=f'''상품 후기를 긍정 또는 부정으로 분류합니다.
# 가격대비좀 부족한게많은듯=부정
# 재구매 친구들이 좋은 향 난다고 해요=긍정
# ㅠㅠ약간 후회가 됩니다..=부정
# 이전에 먹고 만족해서 재구매합니다=긍정
# 튼튼하고 잘 쓸수 있을 것 같습니다. 이 가격에 이 퀄리티면 훌륭하죠='''
# response = kogpt_api(prompt, max_tokens=1, temperature=0.4)
# print(response)
# print(response['generations'][0]['text'])

# #이런거를? 사용자로부터 입력받아서 처리하게 하려면?
# user_input = input('상품평후기를 입력해주세요: ')
# prompt=f'''상품 후기를 긍정 또는 부정으로 분류합니다.
# 가격대비좀 부족한게많은듯=부정
# 재구매 친구들이 좋은 향 난다고 해요=긍정
# ㅠㅠ약간 후회가 됩니다..=부정
# 이전에 먹고 만족해서 재구매합니다=긍정
# {user_input}='''
# response = kogpt_api(prompt, max_tokens=20, temperature=1.0)
# print(response)
# print(response['generations'][0]['text'])

#3. 한줄로 요약하기
# prompt='''카카오(대표이사 정신아)의 카카오프렌즈가 서울페스타 2024에 참여한다고 29일 밝혔다. 서울페스타는 서울시에서 주최하는 서울 대표 봄축제로 서울의 다양한 매력을 전 세계에 홍보하는 행사다. 카카오는 황금연휴 기간 서울 곳곳에서 카카오프렌즈를 활용한 행사로 나들이객들과 관광객들에게 색다른 즐거움을 선사할 계획이다.
# 먼저, 카카오는 5월 1일부터 6일까지 광화문광장에서 라이언과 춘식이로 꾸며진 포토존을 운영한다. 6m가 넘는 초대형 라이언과 춘식이 애드벌룬이 설치돼 축제 분위기를 한껏 살릴 예정이며, 라이언과 춘식이가 그려진 포토카드를 나눠주는 이벤트도 진행한다. 포토카드는 4일을 제외한 매일 11시부터 포토존 앞에서 선착순으로 배부한다.
# 또한, ‘프렌즈와 떠나는 별빛 여행’을 주제로 한강 드론 라이트 쇼를 선보인다. 1,000여 대의 드론이 라이언과 춘식이의 탄생 세계관과 K-컬처를 즐기는 라이언과 춘식이의 모습을 그려내며 한강의 밤하늘을 수놓을 예정이다. 5월 6일 저녁 8시 잠실한강공원에서 관람 가능하며, 자세한 내용은 라이언&춘식 인스타그램에서 확인할 수 있다.
# 한편, 카카오톡 ‘펑’에서 ‘라이언 서울로컬로드’ 콘텐츠도 연재한다. 광화문, 잠실을 시작으로 라이언이 서울의 다양한 지역을 직접 방문하고 소개하는 일상 공유 콘텐츠를 통해 팬들과 실시간으로 소통할 예정이다.
# 최선 카카오 프렌즈크리에이티브 리더는 “K-캐릭터인 카카오프렌즈의 매력을 서울 곳곳에서 발견할 수 있도록 이번 행사를 준비했다” 며 “앞으로도 시민들의 일상 속에 더 가까이 다가갈 수 있도록 카카오프렌즈의 다양한 활동들을 전개할 예정이니 많은 기대 바란다” 라고 전했다.

# 한줄 요약:'''
# response = kogpt_api(prompt, max_tokens=64, temperature=0.1)
# print(response)

#4.질문에 답변하기
# prompt='''의료 스타트업으로 구성된 원격의료산업협의회가 10월부터 열리는 국정감사 시기에 맞춰 국회와 정부에 비대면 진료법 근거 마련을 촉구하는 정책제안서를 제출한다. 코로나19 사태에 비대면 진료의 한시 허용으로 원격 진료, 의약품 배송 등 서비스가 속속 등장하는 가운데 제도화 논의를 서둘러야 한다는 목소리가 높아질 것으로 전망된다. 코리아스타트업포럼 산하 원격의료산업협의회는 '위드(with) 코로나' 방역 체계 전환을 염두에 두고 비대면 진료 제도화 촉구를 위한 공동 대응 작업을 추진하고 있다. 협의회는 닥터나우, 엠디스퀘어, SH바이오, 메디버디 등 의료 스타트업 13개사로 구성됐다. 협의회는 국정감사 시기를 겨냥해 국회와 주무 부처인 보건복지부에 비대면 진료의 법적 근거 마련을 촉구할 방침이다. 이를 위해 주요 의원실과 관련 의견을 교환하고 있다. 협의회는 궁극적으로 의료법과 약사법 개정이 필요하지만 의료법 테두리 안에서 시행령 개정 등으로도 비대면 진료 가능성과 대상·의료기관 등을 구체화할 수 있다는 복안이다. 복지부 장관령으로 비대면 진료 기간을 명시하는 방안 등을 통해 사업 리스크도 줄일 수 있다. 올해 안에 국내 방역체계 패러다임이 바뀔 것으로 예상되는 점도 비대면 진료 제도화의 필요성을 높이고 있다. 최근 코로나19 백신 접종이 속도를 내면서 방역 당국은 위드 코로나 방역체계 전환을 고려하고 있다. 인구 대비 백신 접종 완료율이 70%가 되는 오는 10월 말에는 전환 논의가 수면 위로 뜰 것으로 보인다.
# 정책제안서를 제출하는 시기는 언제인가?:'''

# print('본문\n', prompt)

# user_input = input('다음 본문에서 궁금한 것을 질문하시오: ')
# gpt_prompt = prompt + user_input + "?"

# response = kogpt_api(prompt, max_tokens=128, temperature=0.2)
# print(response['generations'][0]['text'])

#5. 말투바꾸기
user_input = input('당신의 평소 말투대로 대답해주세요: ')

prompt=f'''주어진 문장을 존댓말 문장으로 바꿔주세요.

문장:하지마!
존댓말:하지 말아주세요.

문장:나랑 같이 놀러가자
존댓말:저랑 같이 놀러가지 않으실래요?

문장:배고파 밥줘
존댓말:배가고픈데 밥을 먹어도 될까요?

문장:그거 재밌어?
존댓말:그것은 재미 있나요?

문장:뭐하는거야 지금
존댓말:지금 무엇을 하시는 건가요?

문장:{user_input}
존댓말:'''
response = kogpt_api(prompt, max_tokens=32, temperature=0.7)
print(response['generations'][0]['text'])


