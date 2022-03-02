# 참고 : https://wook-2124.tistory.com/273
# https://tooo1.tistory.com/111

import sys
input = sys.stdin.readline
from collections import deque

def bfs(n):
    queue = deque([n])
    while queue:
        x = queue.popleft()
        if x == k:
            print(dist[x])
            break
        for nx in (x-1,x+1,2*x): # nx = 4, 6, 10
            if 0<=nx<=Max and not dist[nx]: # 같은 수가 중복으로 나오면 안되기 때문에
                dist[nx] = dist[x]+1
                queue.append(nx) # queue = deque([4,6,10])


n, k = map(int,input().split(' ')) # 수빈, 동생
Max = 100000
dist = [0] * (Max+1)
bfs(n)

