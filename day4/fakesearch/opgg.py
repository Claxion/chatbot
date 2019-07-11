import requests
from bs4 import BeautifulSoup as BS

# 1. opgg요청
url = "https://www.op.gg/summoner/userName=cuzz"
# 2. html리턴
res = requests.get(url)
# 3. html 안의 정보를 출력
doc = BS(res.text,"html.parser")

win = doc.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins").text
print(win.replace("W","승"))
print(win[:-1] + "승")
print(win[:3] + "승")
print(win[::-1]) # 뒤집기