# # 시간초과
# num = int(input())
# li = []
# for _ in range(num):
#     dig = int(input())
#     li.append(dig)

# li.sort()
# for i in range(len(li)):
#     print(li[i])


# input이 sys.stdin.readline보다 느리다.

import sys

num = int(input())
li = []
for _ in range(num):
    li.append(int(sys.stdin.readline()))

li.sort()
for i in li:
    print(i)