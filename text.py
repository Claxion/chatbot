#파일 다룰 때 맨처음
#open('파일명','뭐할건지')
# r : read
# w : write
# a : append
f = open('ssafy.txt','w')
for i in range(5) :
    f.write("Hello Ssafy\n")
f.close()

# good "with"!!!! 
# write! 
# with open('ssafy.txt','w', encoding = "utf-8") as f : 
#     for i in range(5) : 
#         f.write("with를 썼다\n")

with open('ssafy.txt','r', encoding="utf-8") as f : 
    #result = f.read() # 전체 한번에 나옴
    result = f.readlines()

    print(result)