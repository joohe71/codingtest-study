# 50점
import sys
input = sys.stdin.readline

n = int(input())
m = int(input()) # S의 길이
s = input()
oi = "OI"
p = "IOI" + oi*(n-1)
cnt = 0

for i in range(m-len(p)):
    if s[i:i+len(p)] == p: # 슬라이싱 사용
        cnt += 1

print(cnt)


# 50점
import sys
input = sys.stdin.readline

n = int(input())
m = int(input()) # S의 길이
s = input()
oi = "OI"
p = "IOI" + oi*(n-1)
cnt = 0

if (s.find("I") != -1 and s.find("I") <= (m-len(p))):
    for i in range(s.find("I"),m-len(p)):
        if s[i:i+len(p)] == p: # 슬라이싱 사용
            cnt += 1

print(cnt)
