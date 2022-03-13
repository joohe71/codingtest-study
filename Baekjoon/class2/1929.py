import sys
input = sys.stdin.readline
n, m = map(int,input().split())
num = list(range(n,m+1))
add = 0

for i in num:
    if i == 2:
        print(i)
    elif i != 1 and i != 2:
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            print(i)


