from flask import Flask, render_template
import random
import requests
from datetime import datetime

app = Flask(__name__)
## __name__ : execution context? 

@app.route("/")
def home() : 
    #return render_template("넘겨주는 템플릿 파일이름")
    return render_template("home.html")

@app.route("/hello/<name>")
def hello(name) : 
    #name에는 hello 이름 활용가능.
    # <name> == empty string 인 경우는 도저히 해결이 불가능한가? 
    if name != None :
        return render_template("hello.html", usename=name)
    else : 
        return render_template("hello.html")

@app.route('/menu')
def menu() : 
    menu = { 
        "짜장면" : "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Jajangmyeon_by_stu_spivack.jpg/240px-Jajangmyeon_by_stu_spivack.jpg" , 
        "떡볶이" : "http://recipe1.ezmember.co.kr/cache/recipe/2016/10/07/f43063e718c49d85ddce4880e4a41fcd1.jpg",
        "피자" : "https://cdn.dominos.co.kr/admin/upload/goods/20180827_pWzUcM5T.jpg", 
     }

    name =  random.choice(list(menu.keys()))
    link = menu[name]
    
    #랜덤 음식메뉴
    #해당 음식사진 
    return render_template('menu.html', name = name, link = link)

#랜덤 넘버를 추천해주고, 최신 로또와 비교하여 등수를 알려주는 기능
@app.route('/lotto')
def lotto() : 
    lotto_weekcount = 1
    # 최신 로또 받아오기
    while True : 
        url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=" + str(lotto_weekcount)
        res = requests.get(url)
        dic_lotto = res.json()
        lottodaystr = dic_lotto['drwNoDate']
        lottodaynums = str(lottodaystr).split("-")

        # 날짜 받아오기
        today = datetime.now().date()
        lottoday = datetime(int(lottodaynums[0]), int(lottodaynums[1]), int(lottodaynums[2]))
        if lottoday.year < today.year :
            lotto_weekcount += 1
            continue 
        elif lottoday.month < today.month : 
            lotto_weekcount += 1 
            continue
        elif lottoday.day < today.day - 7 :
            lotto_weekcount += 1 
            continue
        else : 
            break
    
    winner = []

    # 로또 당첨번호
    for i in range(1,7) : 
        winner.append(dic_lotto['drwtNo'+str(i)])

    #로또 추천
    yours = []
    yours = sorted(random.sample(range(1,46),6))
    samecount = len(set(winner) & set(yours))
    returnstr =  ""
    if  samecount == 6 : 
        returnstr = "현재회차 : " + str(lotto_weekcount) + "\n" + "축하합니다. 1등\n" + "당첨 : " + str(winner) + "\n" + "당신 : " + str(yours) + "\n" + str(today)
    elif samecount == 5 : 
        returnstr = "현재회차 : " + str(lotto_weekcount) + "\n" + "축하합니다. 3등\n" + "당첨 : " + str(winner) + "\n" + "당신 : " + str(yours) + "\n" +str(today)
    elif samecount == 4 : 
        returnstr = "현재회차 : " + str(lotto_weekcount) + "\n" + "축하합니다. 4등\n" + "당첨 : " + str(winner) + "\n" + "당신 : " + str(yours) + "\n" + str(today)
    elif samecount == 3 : 
        returnstr = "현재회차 : " + str(lotto_weekcount) + "\n" + "축하합니다. 5등\n" + "당첨 : " + str(winner) + "\n" + "당신 : " + str(yours) + "\n" + str(today)
    else :
        returnstr = "현재회차 : " + str(lotto_weekcount) + "\n" + "꽝입니다.\n" + "당첨 : " + str(winner) + "\n" + "당신 : " + str(yours)
    
    return returnstr

    
    

#그냥 쓰려면 git에서 flask run
#자동 재시작 : python app.py로 실행 
if __name__ == '__main__' :
    app.run(debug = True)

