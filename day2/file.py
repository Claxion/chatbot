# 파일 관리 연습
import os

# listdir :  git bash : ls 폴더 내 파일리스트 보여주기
# print(os.listdir())

# rename  : git bash : mv (해당 파일명) (바꿀 파일명)
# os.rename("hello.py", "replace.py")

# chdir : dir 위치 변경

# system : 파이썬 안에서 커맨드 사용하기 
#print(os.system('ls'))
#os.system('touch a.txt')
#os.system('rm a.txt')
#os.system('cd report')
#os.chdir('..') 상위폴더 돌아가기

os.chdir('report')
#파일생성 100번 반복
#for i in range(100) : 
    #os.system('touch report%s.txt' % str(i))
    #os.system(f'touch report{i}.txt') #f-string (3.6부터 지원)
#    os.system('touch report{0}.txt'.format(i))

files = os.listdir()

for name in files : 
    os.rename(name, name.replace("samsung","ssafy"))
    #os.replace
