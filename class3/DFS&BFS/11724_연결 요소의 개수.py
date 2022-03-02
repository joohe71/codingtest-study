# 중요한것이 python은 재귀제한이 걸려있기 때문에 재귀 허용치가 넘어가면 런타임에러를 일으킨다. 때문에 sys.setrecursionlimit(10000) 처럼 작성해야 한다. => https://fuzzysound.github.io/sys-setrecursionlimit

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n,m = map(int,input().split(" ")) #점의 개수, 연결 개수
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int,input().split(' '))
    graph[x].append(y)
    graph[y].append(x)

visited = [False]* (n+1)

def dfs(v):
    visited[v] =True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

cnt = 0
for j in range(1,n+1):
    if not visited[j]:
        dfs(j)
        cnt += 1

print(cnt)