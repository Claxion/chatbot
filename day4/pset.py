# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
sum1 = 0
for k,v in score.items() : 
    sum1 += v

print('==== Q1-1 ====')
print(sum1 / len(score.keys()))

# print(list(babos.keys()))
# print(list(babos.values()))

# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')
sum1  =0 
count = 0
for key in scores.keys() : 
    for k,v in scores[key].items() : 
        sum1 += v 
        count += 1 

print(f"전체 평균은 : {sum1/count}")

# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')

for citykey in city.keys() : 
    print("{0}의 평균온도 : {1}".format(citykey, str(sum(city[citykey])/3)))

# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')

maxcity = dict()
mincity = dict() 
for k,v in city.items() : 
    maxcity[k] = max(v)
    mincity[k] = min(v)

for k in maxcity.keys() :
    if maxcity[k] == max(maxcity.values()) :
        print("가장 더운 곳 :" + k)
        break
    
for k in mincity.keys() :
    if mincity[k] == min(mincity.values()) :
        print("가장 추운 곳 :" + k)
        break


# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')
if 2 in city['서울'] :
    print(True)
else : 
    print(False)
