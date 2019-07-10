# 1. problem.txt 생성 후 , 다음과 같은 내용을 작성
# 0
# 1
# 2
# 3

#2. 1의 txt를 순서를 뒤집자


#1.
with open("problem.txt","w") as f : 
    for i in range(4) :
        f.write(str(i)+ "\n")

#2. 
# reverse() 함수는 리턴값이 없고 원본 변경

with open("problem.txt","r") as f : 
    result = f.readlines()
    
with open("problem.txt","w") as f :
    result.reverse()
    for i in result :
        f.write(str(i))

#3
with open("problem.txt","w") as f : 
    result.reverse()
    f.writelines(result)

