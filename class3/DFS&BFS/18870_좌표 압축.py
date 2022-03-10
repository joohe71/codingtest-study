# 시간초과 이유 => list.index(i)의 형태는 시간복잡도 O(N)
# index(i)의 형태는 시간복잡도 O(1)

# import sys
# input=sys.stdin.readline
# n = int(input())
# m = list(map(int,input().split(' ')))
# m1 = list(set(m))
# m1.sort()
# result=[]
# for j in m:
#     result.append( m1.index(j))

# print(*result)

# =============================

import sys
input=sys.stdin.readline
n = int(input())
m = list(map(int,input().split(' ')))
m1 = list(set(m))
m1.sort()
result=[]
dict = {m1[i] : i for i in range(len(m1))}

for j in m:
    print(dict[j], end=" ")

