from flask import Flask, render_template
import requests
import datetime
import random 

app = Flask(__name__)

@app.route("/lotto")
def lotto() :
    count = 0 
    winnum = [] 
    mynum = []
    msg = 0

    today = datetime.datetime.now()
    stat_day = datetime.datetime(year = 2002, month = 12, day = 7)
    count = (today - stat_day).days//7+1

    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=" + str(count)
    res = requests.get(url)
    dict_lotto = res.json()
    
    # 로또 당첨번호
    for i in range(1,7) : 
        winnum.append(dict_lotto['drwtNo'+str(i)])

    # 내 번호 
    mynum = sorted(random.sample(range(1,46),6))

    samenum = len(set(winnum) & set(mynum))
    if samenum == 6 : 
        msg = "1등입니다!"
    elif samenum == 5 : 
        msg = "3등입니다!"
    elif samenum == 4 : 
        msg = "4등입니다!"
    elif samenum == 3 :
        msg = "5등입니다!"
    else : 
        msg = "꽝입니다."



    return render_template('lotto.html', count = count, winnum = winnum, mynum = mynum, msg = msg)


if __name__ == "__main__"  : 
    app.run(debug=True)
