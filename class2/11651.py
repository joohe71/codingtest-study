# 116750과 다른 방법 - 시간 효율적
import sys
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(tuple(map(int,sys.stdin.readline().split())))

arr.sort(key=lambda x: (x[1],x[0]))
for i in range(len(arr)):
    print(arr[i][0],arr[i][1], sep=" ")

