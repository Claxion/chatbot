import json
import requests

# using slack 

#오늘의 식사 시간 
#오늘의 메뉴 A, B 
#메뉴가 하나일 경우에는 하나만
# content에 입력
# 0 : 월 1 : 화 2 : 수 3 : 목 4 : 금 

def sendMenuByDay(theDay):
    # test 채널에 webhook으로 메시지를 보낸다.
    if theDay == 5 or theDay == 6 : 
        return
    else :
        webhook_url = "https://hooks.slack.com/services/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"
        content = "안녕하세요"
        payload = {"text": content}
    
        requests.post(
            webhook_url, data=json.dumps(payload),
            headers={'Content-Type': 'application/json'}
        )