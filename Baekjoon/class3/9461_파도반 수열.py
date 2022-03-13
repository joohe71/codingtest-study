# Sn = Sn-1 +Sn-5

import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    m= int(input())
    arr = [1,1,1,2,2]
    for i in range(5,m):
        arr.append(arr[i-5]+arr[i-1])
    print(arr[m-1])

