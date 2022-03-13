# 힙에 튜플(tuple)를 원소로 추가하거나 삭제하면, 튜플 내에서 맨 앞에 있는 값을 기준으로 최소 힙이 구성되는 원리를 이용하는 것입니다.

import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    num = int(input())
    if num == 0:
        if(arr):
            print(heapq.heappop(arr)[1]) # max 양수값 출력
        else:
            print(0)
    else:
        heapq.heappush(arr,(-num,num)) # 튜플 (음수,양수) => 음수 값 기준으로 오름차순 정리