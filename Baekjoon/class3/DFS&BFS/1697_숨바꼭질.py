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

# ===================================================
# 새로운 정답

import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int,input().split(' '))
visited = [0]*100001

def bfs(v):
    queue = deque([v])
    while queue:
        a = queue.popleft()
        if a == k:
            break
        for i in (a-1,a+1,2*a):
            if 0<=i<=100000:
                if visited[i]==0:
                    queue.append(i)
                    # print(queue)
                    visited[i]=visited[a]+1
    return visited

print(bfs(n)[k])