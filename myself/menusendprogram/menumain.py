# 여기서 관련 코드를 총괄한다. 
# opencv 이용해서 그림을 흑백으로 변경 
# 흑백 그림에서 opencv 이용해서 박스를 찾음
# 박스를 각각 찾아서 해당 박스의 위치를 가지고 그림을 분할함
# 각 그림에서 분할한 데이터를 가지고 pytesseract 를 가지고 글자인식
# 글자 인식한 것을 slack을 통해서 전달


# 전달하는 부분은 해당 일에 맞는 메세지를 전달
# 필요한 데이터는 1주일마다 edussafy 게시판을 확인해서 새로운 그림을 받아옴. 여기에서는 selenium을 이용해서 로그인과 가져오는 것까지 한다.

import datetime


import menugetter 
import menumaker
import menusender


# 체크 필요없이 월요일이면 새로 접속해서 가져오고 화~금은 기존의 데이터를 사용한다. 
# datetime의 weekday 월 0 ~ 일 6
weekdayNum = datetime.datetime.now().weekday()
menuInfo = {}
# menuInfo = { 
#     0: 
#     { 
#     'A' : ["된장국","쌀밥"],
#     'B' : ['미역국','보리밥']
#     }
#     1 : 
# }

if weekdayNum == 6 : 
    address = r"C:\Users\student\Downloads"
    menugetter.getMenuImage(address)  #img는 그냥 안에서 저장하는 것으로 끝
    # 그림 address만 넘기자
    # Downloads 혹은 다른 위치가 좋음.
    
    #menuInfo = 
    #menumaker.makeMenuItems(address)


# if weekdayNum in range(0,5) : 
#     pass
#     # menuInfo[weekdayNum]
#     #menusender.sendMenuByDay(theDay, menus)
# else : #주말
#     pass


