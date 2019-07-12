from flask import Flask , render_template, request
import telegram
from decouple import config
import requests
import random
import papago

app = Flask(__name__)
token = config("TELEGRAM_TOKEN")

@app.route("/")
def home() : 
    return render_template('home.html')

@app.route("/send", methods = ['GET'])
def sendmessage() : 
    message = request.args.get("message")
    telegram.sendMessage(message)
    return render_template('send.html', message = message)

#get & post : 웹에서 요청을 보낼 때의 양식
#get : url에 모든 정보를 심어서 보낸다
#post : 정보가 노출되지 않아야 할 때
@app.route(f'/{token}', methods =['POST'])
def webhook() : 
    # 1. 메아리챗봇
    # (1) 웹훅을 통해 telegram이 보낸 요청 안에 있는 메세지를 가져와 
    # (2) 그대로 전송
    res = request.get_json() 
    text = res.get('message').get('text')
    chat_id = res.get('message').get("chat").get("id")
    base = "https://api.telegram.org"
    method = "sendMessage"
    
    if res.get("message").get("photo") is not None :
        # 사진임 => 유명인 얼굴인식 ㄱㄱ 
        file_id = res.get("message").get("photo")[-1].get('file_id')
        
        file_res = requests.get(f"{base}/bot{token}/getFile?file_id={file_id}")
        file_path = file_res.json().get("result").get("file_path")
        file_url = f"{base}/file/bot{token}/{file_path}"
        image = requests.get(file_url, stream= True)

        client_id = config("NAVER_ID")
        client_secret = config("NAVER_SECRET")
        # url = "https://openapi.naver.com/v1/vision/face" # 얼굴감지
        url = "https://openapi.naver.com/v1/vision/celebrity" # 유명인 얼굴인식
        files = {'image': image.raw.read()}
        headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
        clova_res = requests.post(url,  headers=headers, files=files)
        text = clova_res.json().get("faces")[0].get("celebrity").get("value")   
    else : 
        if text == "lotto" :
            lotto = sorted(random.sample(range(1,46), 6))
            text = lotto
        #elif text[0:3] == "/번역" :
            #papago로 네이버 번역 결과를 알려준다.
        #    beforetranslatetext = text[3:].lstrip()
        #    text = papago.papagoTranslate(beforetranslatetext)
            
        
                
    url = f"{base}/bot{token}/{method}?chat_id={chat_id}&text={text}"
    requests.get(url)
    

    return '', 200

if __name__ == "__main__" : 
    app.run(debug=True)