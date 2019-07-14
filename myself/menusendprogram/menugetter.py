# 메뉴를 인터넷에서 가져오는 프로그램
# 완전 작업 안함
# chrome driver가 없을 경우에는 chrome driver 설치 작업까지 진행해줘야 한다. 
# 필요로 하는 위치에 img 다운로드


import requests
import bs4
from selenium import webdriver
import urllib

def getMenuImage() :
    chromedriver_dir = r'C:\Users\student\Downloads\chromedriver_win32\chromedriver.exe'
    driver = webdriver.Chrome(chromedriver_dir)

    inputusername = "" #사용자이름
    inputuserpwd  = "" #사용자 비밀번호

    loginurl = "https://edu.ssafy.com/comm/login/SecurityLoginForm.do"
    driver.get(loginurl)
    username = driver.find_element_by_id("userId")
    username.clear()
    username.send_keys(inputusername)
    password = driver.find_element_by_id("userPwd")
    password.clear()
    password.send_keys(inputuserpwd)

    #driver.find_element_by_name("로그인").click()
    #driver.find_element_by_link_text("로그인").click()
    #driver.find_element_by_class_name("form-btn").click()
    driver.find_element_by_css_selector("#wrap > div > div > div.section > form > div > div.field-set.log-in > div.form-btn > a").click()

    #로그인 과정 완료 후 공지사항으로 이동.
    
    noticeurl = "https://edu.ssafy.com/edu/board/notice/list.do"
    #noticeurl = "https://edu.ssafy.com/edu/board/notice/detail.do?searchBrdItmCdVal=&brdItmSeq=2588&searchWord=&_csrf=10ab5067-ff1d-4da5-b60f-b809db80124c&pageIndex=1"
    driver.get(noticeurl)
    # 공지사항에서 <중식시간>이라는 글을 찾아서 가장 번호가 높은 것을 받아내자.
    
    html = driver.page_source
    # 왜 res.text = "" ? 비어있어서 뒤로 진행이 안됨. js 때문인가? 
    # driver 를 통해서 직접 가져오자.
    doc = bs4.BeautifulSoup(html, 'html.parser')
    # 공지사항 아래의 것들을 가져온다.
#     position = "#wrap > form > div > div.content > div.section > div.board-wrap > table.default-tbl.type2 > tbody > tr"
#     notices = doc.select(position)
#     #notices = doc.select("td > span")
#     launches = []
#     for notice in notices :
#          if "중식" in notice.text :
#               launches.append(notice)
    
    # launches[0] 가 최신
    launchgoal = driver.find_element_by_css_selector("#wrap > form > div > div.content > div.section > div.board-wrap > table.default-tbl.type2 > tbody > tr:nth-child(1) > td.link > a").click()

    # 들어가는 것까지는 동작.
    html = driver.page_source
    doc = bs4.BeautifulSoup(html,'html.parser')
    print(doc)
    imageurl = ""

    for img in bs4.BeautifulSoup.find_all("img") : 
         img_src = img.get("src")
         img_url = "http:" + img_src
         img_name = img_src.replace("/","")

         urllib.request.urlretrieve(img_url,"./img/"+ img_name)
         print(img_src)
         print(img_url)
         print(img_name)
    
     
    #css #wrap > form > div > div.content > div.section > div.board-wrap > table.default-tbl.type2 > tbody > tr:nth-child(1) > td.link > a
    #wrap > form > div > div.content > div.section > div.board-wrap > table.default-tbl.type2 > tbody > tr:nth-child(2) > td.link > a
    #xpath # //*[@id="wrap"]/form/div/div[2]/div[2]/div[1]/table[2]/tbody/tr[1]/td[2]/a

    # 위치를 찾았다고 가정하고 .. 들어가서 그림 다운받기


# td class="num tac hidden-field"><span>3</span></td>
# <td class="link">
# <a href="#;" onclick="fnDetail('2588');">[기타] 2019년 07월 3주차 식단 및 반별 중식시간 안내</a>
# </td>
# <td class="date tac"><span>2019.07.12</span></td>
# </tr>
# <tr>
# <td class="num tac hidden-field"><span>2</span></td>
# <td class="link">
# <a href="#;" onclick="fnDetail('2505');">[기타] 2기 입학식 후기 SNS 이벤트 당첨자 발표</a>
# </td>
# <td class="date tac"><span>2019.07.09</span></td>
# </tr>
# <tr>
# <td class="num tac hidden-field"><span>1</span></td>
# <td class="link">
# <a href="#;" onclick="fnDetail('2418');">[기타] 2019년 07월 2주차 식단 및 반별 중식시간 안내</a>
# </td>
# <td class="date tac"><span>2019.07.08</span></td>





    # 찾아냈다면 해당되는 페이지를 클릭해 내부 진입 후 그림을 찾아 다운로드한다.
    

    #xpath = '//*[@id="_mainComunityId"]/div[2]/div[1]/article/a/span' # 알림
    #xpath = '//*[@id="checkOut"]/span'   #퇴실
    #xpath = '//*[@id="checkIn"]/span' #입실

    #btn = driver.find_element_by_xpath(xpath)
    # 자바 스크립트가 있을 경우에는 실행 코드를 넣어줘야함.
    # http://blog.naver.com/PostView.nhn?blogId=kiddwannabe&logNo=221430636045&categoryNo=0&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView
    #driver.execute_script("arguments[0].click();", btn)



if __name__ == "__main__" :
     getMenuImage()
