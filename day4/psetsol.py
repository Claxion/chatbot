# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1-1 ====')

# 합계 구하기
print(sum(score.values()) / len(score.keys()))


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
aaver = sum(scores['a'].values()) / len(scores['a'].values())
baver = sum(scores['b'].values()) / len(scores['b'].values())
print(aaver)
print(baver)


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

for temp in city.values() : 
    print(sum(temp) /len(temp))

# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')
# 플래트닝 : list in list -> one list  : numpy에서 제공하는 함수 or itertools : 
maxes = [] 
mins = [] 
for temp in city.values() : 
    maxes.append(max(temp))
    mins.append(min(temp))
high = max(maxes)
low = min(mins)

for k,v in city.items() : 
    if high in v : 
        print(k)
    if low in v : 
        print(k)



# 웬만한 로직보다 효율적임

# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')
if 2 in city['서울'] :
    print(True)
else : 
    print(False)
