import sys
import heapq  # heapq모듈 사용
input = sys.stdin.readline

arr=[]
num = int(input())
for _ in range(num):
    m = int(input())
    if m != 0:
        heapq.heappush(arr,(abs(m), m)) # 튜플 (절대값,기존값) => 절대 값 기준으로 오름차순 정리
    else:
        if(arr):
            print(heapq.heappop(arr)[1])
        else:
            print(0)



 