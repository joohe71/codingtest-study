# 학생들이 추천을 시작하기 전에 모든 사진틀은 비어있다.
# 어떤 학생이 특정 학생을 추천하면, 추천받은 학생의 사진이 반드시 사진틀에 게시되어야 한다.
# 비어있는 사진틀이 없는 경우에는 현재까지 추천 받은 횟수가 가장 적은 학생의 사진을 삭제하고, 그 자리에 새롭게 추천받은 학생의 사진을 게시한다. 이때, 현재까지 추천 받은 횟수가 가장 적은 학생이 두 명 이상일 경우에는 그러한 학생들 중 게시된 지 가장 오래된 사진을 삭제한다.
# 현재 사진이 게시된 학생이 다른 학생의 추천을 받은 경우에는 추천받은 횟수만 증가시킨다.
# 사진틀에 게시된 사진이 삭제되는 경우에는 해당 학생이 추천받은 횟수는 0으로 바뀐다.

import sys
input= sys.stdin.readline
n = int(input())
m = int(input())
rec = list(map(int,input().split(' ')))
picture = {}
cnt=0
for i in rec:
    cnt+=1
    if len(picture)<n:
        if i not in list(picture.keys()):
            picture[i]=[1,cnt] # [추천 횟수,게시 순서]
            # print(picture)
        else:
            picture[i][0]+=1
            # print(picture)
    else:
        if i in list(picture.keys()):
            picture[i][0]+=1
            # print(picture)
        else:
            new_picture = sorted(picture.items(),key=lambda x:(x[1][0],x[1][1]))
            del picture[new_picture[0][0]]
            picture[i]=[1,cnt] # [추천 횟수,게시 순서]
            # print(picture)

result = sorted(picture.items(),key=lambda x:x[0])
print(*[x[0] for x in result])

