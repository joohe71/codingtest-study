# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.

# 1 -> 0
# 2 -> 1
# 3 -> 1
# 4 -> 2
# 5 -> 3
# 6 -> 2
# ...
# 9 -> 2
# 10 -> 3
# f(n) = min(f(n-1),f(n/3),f(n/2))+1
# 다이나믹 프로그래밍(바텀업 방식)
import math,sys
input = sys.stdin.readline
def solve():
    n = int(input())
    arr = [0,0,1,1,2]
    for i in range(5, n+1):
        one, two, three = math.inf, math.inf, arr[i-1] #2나 3으로 나누어 지지 않을 수도 있기 때문에
        if i % 3 == 0:
            one = arr[i//3]
        if i % 2 == 0:
            two = arr[i//2]
        arr.append(1+min(one,two,three))
     
    print(arr[n])

solve()