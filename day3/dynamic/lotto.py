#lotto api를 통해 최신 당첨번호를 가져온다. 
import requests
import random

url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866"
res = requests.get(url)
# json 형태로 리턴됨. 리턴된 결과물을 python dictionary로 변경
# json 파일을 파이썬 딕셔너리로 바꿔줌
json_lotto = res.text
dict_lotto = res.json()

#print(dict_lotto['drwtNo4']) # 딕셔너리 => not error
# print(json_lotto['drwtNo4']) # str => occur error 

winner = []
#당첨까지 필요한 횟수 계산
for i in range(1,4) : 
    winner.append(dict_lotto['drwtNo'+str(i)])

# print("당첨 : " + str(winner))
# count = 0
# iswin = False
# while iswin == False : 
#     mylotto = sorted(random.sample(range(1,46), 3))
#     print("내 로또 : " + str(mylotto))
#     if mylotto != winner : 
#         count += 1 
#     else  :
#         iswin = True

# print("당첨 : " + str(winner))
# print("내 로또 : " + str(mylotto))
# print(str(count)+"번만에 당첨")

# for i in range(1,7) : 
#     winner.append(dict_lotto['drwtNo'+str(i)])

# print("당첨 : " + str(winner))
# mylotto = sorted(random.sample(range(1,46), 6))
# print("내 로또 : " + str(mylotto))
count = 0
while True : 
    same = 0 
    count += 1
    print(count)
    mylotto = sorted(random.sample(range(1,46), 3))
    print("내 로또 : " + str(mylotto))
    for wnum in winner : 
        for mynum in mylotto : 
            if wnum == mynum : 
                same += 1
                
    
    if same == 6 :
        print("1등입니다.")
        print("당첨 : " + str(winner))
        print("내 로또 : " + str(mylotto))
        print(count + "번 만에 당첨")
        break

# 멋진 방법
#count = len(set(winner) & set(your_lotto))