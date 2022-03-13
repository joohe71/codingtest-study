# 참고 : https://doorbw.tistory.com/58

import sys
input = sys.stdin.readline
a = int(input())
for _ in range(a):
    fibo = int(input()) # 피보나치(fibo)
    zero = [1,0,1]
    one = [0,1,1]
    length = len(zero)
    if fibo <= 2:
        print(zero[fibo],one[fibo])
    if length <= fibo:
        for i in range(length,fibo+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
        print(zero[-1],one[-1])
