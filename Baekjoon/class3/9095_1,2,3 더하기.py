# 1: 1
# 2: 1+1  2
# 3: 1+1+1  1+2  2+1  3
# 4: 1+3  1+1+2  2+2  1+1+1+1  1+2+1 2+1+1  3+1
# f(4) = f(3) + f(2) + f(1)
# f(n) = f(n-1) + f(n-2) + f(n-3)

import sys
input = sys.stdin.readline
n= int(input())
for _ in range(n):
    m = int(input())
    f = [1,2,4]
    for i in range(3,m):
        f.append(f[i-1]+f[i-2]+f[i-3])
    print(f[m-1])