# 시간 초콰
# import sys
# input = sys.stdin.readline
# n = int(input())
# arr = []
# for _ in range(n):
#     num = int(input())
#     if num > 0 :
#         arr.append(num)
#     elif num == 0:
#         if (arr):
#             arr.sort()
#             print(arr.pop(0))
#         else:
#             print(0)
    
# -------------------------------------
# heapq 모듈은 이진 트리(binary tree) 기반의 최소 힙(min heap) 자료구조를 제공합니다.


import heapq  # heapq모듈 사용
import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    num = int(input())
    if num == 0:
        if(arr):
            print(heapq.heappop(arr)) # 가장 작은 원소를 삭제 후에 그 값을 리턴합니다.
        else:
            print(0)
    else:
        heapq.heappush(arr,num)
