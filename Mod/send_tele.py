import telegram
import time

telegram_config = {}
# config 파일 읽기
with open('telegram_config', 'r') as f:
    # 모든 줄 읽어오기
    configs = f.readlines()
    # 한 줄씩 확인해서
    for config in configs:
        # 줄바꿈기호 제거(\n) 후 =로 문자열 분리
        # key, value로 언패킹 (2개 나올것이 확실하기 때문에)
        key, value = config.rstrip().split('=')
        # config 딕셔너리에 키-값 추가
        telegram_config[key] = value

token = telegram_config['token']


bot = telegram.Bot(token)

updates = bot.get_updates()

chat_id = updates[-1].message.chat.id

last_id = updates[-1].update_id

# 서버에서 텔레그램 메시지 확인, 응답 보내기
bot.send_message(chat_id, '아파트 단지 시세조회 시작\n수색/문래6가/여의도/대치 중에 한곳을 입력하세요\n예>대치')
while True:
    
    try:
        # 신규 메시지가 없을 경우 에러가 발생 
        # list index out of range
        # 따라서, try - except 문으로 묶어줌
        
        new_message = bot.get_updates(offset=last_id)[-1]

        if new_message.message.text == '대치':
            # 관련 메시지 발송
            bot.send_document(chat_id, open('/./gitsmw/Agora/Legion/대치.xlsx', 'rb'))
        
        elif new_message.message.text == '수색':
            bot.send_document(chat_id, open('/./gitsmw/Agora/Legion/수색.xlsx', 'rb'))

        elif new_message.message.text == '문래6가':
            bot.send_document(chat_id, open('/./gitsmw/Agora/Legion/문래6가.xlsx', 'rb'))

        elif new_message.message.text == '여의도':
            bot.send_document(chat_id, open('/./gitsmw/Agora/Legion/여의도.xlsx', 'rb'))

        # offset 값 최신화 (update_id) + 1 해줘서 그 다음부터 메시지부터 확인하도록
        last_id = new_message.update_id + 1
    except:
        pass

    # 텔레그램 서버 부하 줄이기 위해 3초마다 확인
    time.sleep(3)



