import sys
from collections import deque
input = sys.stdin.readline
case = int(input())

for _ in range(case):
    n, m = map(int,input().split()) #문서의 개수, 궁금한 문서의 순서
    imp = list(map(int,input().split())) #중요도
    q = deque()
    for i, x in enumerate(imp):
        q.append((i,x))
    
    count = 0
    imp.sort()

    while q:
        i, x = q.popleft()
        if x == imp[-1]:
            imp.pop()
            count += 1
            print(q)
            if i == m:
                print(count)
                break
        else:
            q.append((i,x))
