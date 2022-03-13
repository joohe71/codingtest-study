import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int,input().split())
arr = deque()


for i in range(1,n+1):
    arr.append(i)

print("<",end="")

while(len(arr)>1):
    for j in range(k-1):
        arr.append(arr.popleft())
    print(str(arr.popleft())+", ", end="")
print(str(arr.pop())+">")

