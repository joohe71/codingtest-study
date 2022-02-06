import sys
from collections import Counter
# Counter는 사전(dict) 클래스의 하위 클래스로 리스트나 튜플에서 각 데이터가 등장한 횟수를 사전 형식으로 돌려준다.
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    num = int(sys.stdin.readline())
    arr.append(num)
arr.sort()

print(round(sum(arr)/n)) # 평균
print(arr[n//2]) # 중앙값

cnt = Counter(arr)
mode = cnt.most_common() #등장한 횟수를 내림차순 정렬
if n == 1:
    print(num)
elif mode[0][1] == mode[1][1]:
    print(mode[1][0]) #최빈값
else:
    print(mode[0][0]) #최빈값

print(max(arr)-min(arr)) #범위
