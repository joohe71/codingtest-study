import sys
input = sys.stdin.readline

n = int(input())
arr = [1,3]
for i in range(2,n):
    arr.append(2*arr[i-2]+arr[i-1])
print(arr[n-1]%10007)