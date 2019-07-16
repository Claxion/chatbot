# 메뉴를 인터넷에서 가져오는 프로그램
# 완전 작업 안함
# chrome driver가 없을 경우에는 chrome driver 설치 작업까지 진행해줘야 한다. 
# 필요로 하는 위치에 img 다운로드


import requests
import bs4
from selenium import webdriver
import urllib
from decouple import config


def getMenuImage(address) :
    chromedriver_dir = r'C:\Users\student\Downloads\chromedriver_win32\chromedriver.exe'
    driver = webdriver.Chrome(chromedriver_dir)

    inputusername = config("USERID") #사용자이름
    inputuserpwd  = config("USERPASSWORD") #사용자 비밀번호

    loginurl = "https://edu.ssafy.com/comm/login/SecurityLoginForm.do"
    driver.get(loginurl)
    username = driver.find_element_by_id("userId")
    username.clear()
    username.send_keys(inputusername)
    password = driver.find_element_by_id("userPwd")
    password.clear()
    password.send_keys(inputuserpwd)

    #driver.find_element_by_name("로그인").click()
    driver.find_element_by_css_selector("#wrap > div > div > div.section > form > div > div.field-set.log-in > div.form-btn > a").click()


    #로그인 과정 완료 후 공지사항으로 이동.
    noticeurl = "https://edu.ssafy.com/edu/board/notice/list.do"
    driver.get(noticeurl)
    # 공지사항에서 <중식시간>이라는 글을 찾아서 가장 번호가 높은 것을 받아내자.
    
    html = driver.page_source
    # 왜 res.text = "" ? 비어있어서 뒤로 진행이 안됨. js 때문인가? 
    # driver 를 통해서 직접 가져오자.
    doc = bs4.BeautifulSoup(html, 'html.parser')
    # 공지사항 아래의 것들을 가져온다
    # 어떻게 찾은 위치로 들어가게 할 수 있지 ?.
    # # > tbody > tr" : 여기까지 쓰면 셀레니움이 꺼져버림...??? 단순 크래시의 문제는 버전 문제일수도???
    position = "#wrap > form > div > div.content > div.section > div.board-wrap > table.default-tbl.type2 > tbody" 
    noticebox = doc.select_one(position)
    #print(noticebox)
    notices = noticebox.find_all("tr")
    #print(notices)

    launches = []
    for notice in notices :
         if "중식" in notice.text :
              launches.append(notice)
    
    # launches[0] 가 최신
    # 찾아냈다면 해당되는 페이지를 클릭해 내부 진입 후 그림을 찾아 다운로드한다.
    target = launches[0].a['onclick'] # onclick attribute에 해당되는 값을 받는다.
    # target : fnDetail('2588'); 함수
    driver.execute_script(target)

    html = driver.page_source
    doc = bs4.BeautifulSoup(html,'html.parser')
    #tr:nth-child of 와 같은 식으로 사용할 수 없다. nth-of-type처럼 사용해야 beautiful soup에서 인식가능
    imagebox =  doc.select_one("#wrap > form > div > div.content > div > div:nth-of-type(1) > div.datail-content.mb20 > p > img")
    imageurl = imagebox['src']
    
    res = urllib.request.urlretrieve("https:" + imageurl, address +"\menu.png")

if __name__ == "__main__" :
     address = r"C:\Users\student\Downloads"
     getMenuImage(address)
