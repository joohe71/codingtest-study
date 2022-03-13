#                               10  20  15  25  10  20
#                           0   1   2   3   4   5   6
# 다음계단으로 갈 수 없는 애   0   10  30  35  50  65  65
# 다음계단으로 갈 수 있는애    0   0   20  25  55  45  75

# f(x) = max(g(x), h(x))
# g(x) = h(x-1) + arr[x]
# h(x) = max(g(x-2),h(x-2)) + arr[x]
#      = f(x-2) + arr[x]

import sys
input =sys.stdin.readline

n = int(input())
arr = [0]
for _ in range(n):
    x = int(input())
    arr.append(x)

g  = [0, 0]
h  = [0, arr[1]]

for i in range(2,n+1):
    g.append(h[i-1]+arr[i])
    h.append(max(h[i-2],g[i-2])+arr[i])

print(max(g[-1],h[-1]))