# 시간초과
# import sys
# input = sys.stdin.readline
# n,m = map(int,input().split(' '))
# arr = list(map(int,input().split(' ')))
# for _ in range(n):
#     result = 0
#     i,j = map(int,input().split(' '))
#     for k in range(i-1,j):
#         result += arr[k]
#     print(result)

# ==============================


import sys
input = sys.stdin.readline
n,m = map(int,input().split(' '))
arr = list(map(int,input().split(' ')))
sum_value = 0
prefix_sum = [0]

for y in arr:
    sum_value+=y
    prefix_sum.append(sum_value)

for _ in range(n):
    i,j = map(int,input().split(' '))
    print(prefix_sum(j)-prefix_sum(i-1))