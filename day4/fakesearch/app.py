from flask import Flask, render_template , request
from faker import Faker
import random
import requests
from bs4 import BeautifulSoup as BS

# 응답하는 가짜 구글을 만들자.
fake = Faker("ko_KR") # python faker : 가짜 정보 생성해주는 패키지

# 서버 스타트
app = Flask(__name__)
namejobdic = dict() 
baboyoudic = dict()
percent = dict()


@app.route("/")
def home() : 
    return render_template('home.html')

@app.route("/pastlife")
def pastlife() : 
    return render_template('pastlife.html')

@app.route("/result")
def result() : 
    name =  request.args.get("name")
    job = fake.job()
    if name in namejobdic : 
        job = namejobdic[name]
    else : 
        namejobdic[name] = job
    
    return render_template('result.html', name= name, job= job)

@app.route("/goonghap")
def goonghap() :
    return render_template('goonghap.html')

@app.route("/destiny")
def destiny() : 
    babo = request.args.get("babo")
    you = request.args.get("you")
    #goonghap = random.choice(range(51,101))
    goonghap = random.randint(51,100)

    # dict made by tuple
    # if (babo,you) in baboyoudic :
    #     goonghap = baboyoudic[(babo,you)]
    # else :
    #     baboyoudic[(babo,you)] = goonghap

    # dict in dict 
    if babo in baboyoudic : 
        if you in baboyoudic[babo] :
            goonghap = baboyoudic[babo][you]
        else :
            baboyoudic[babo][you] = goonghap
    else :
        baboyoudic[babo] = dict({you : goonghap})

    # 1. 이름 + 이름으로 저장
    # if babo+you in baboyoudic : 
    #     percent = baboyoudic[babo+you]
    # else : 
    #     percent = random.randint(51,100)

    # 2. dict in dict
    #percent = random.randint(51,100)
    # if babo in baboyoudic : 
    #     if you in baboyoudic[babo] : 
    #         percent = baboyoudic[babo][you]
    #     else : 
    #         baboyoudic[babo][you] = percent
    # else : 
    #     baboyoudic[babo] = {you : percent}

    return render_template('destiny.html', babo = babo, you = you, goonghap= goonghap)

@app.route("/admin")
def admin() :
    #for k,v in baboyoudic.items() : 
    return render_template('admin.html', baboyoudic = baboyoudic)

@app.route("/opgg")
def opgg() : 
    return render_template('opgg.html')


@app.route("/lolresult")
def lolresult() : 
    id = request.args.get("id")
    print(id)
    url = "https://www.op.gg/summoner/userName="
    res = requests.get(url+id)
    doc = BS(res.text,"html.parser")
    win = doc.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins").text
    lose = doc.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses").text
    return render_template('lolresult.html', win = win[:-1] , lose = lose[:-1])

if __name__ == '__main__' : 
    app.run(debug=True)