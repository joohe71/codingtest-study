# n

# 1 : 1
# 2 : 2
# 3 : 3
# 4 : 2+3
# d[n] = d[n-1] + d[n-2]

import sys
input = sys.stdin.readline

n = int(input())
arr = [1,2]
for i in range(2,n):
    arr.append(arr[i-2]+arr[i-1])
print(arr[n-1]%10007)