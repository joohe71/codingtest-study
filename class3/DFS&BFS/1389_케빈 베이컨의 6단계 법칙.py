import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int,input().split(' ')) #유저의 수, 친구관계의 수
graph = [[] for _ in range(n+1)]

visited = [False] * (n+1)
for _ in range(m):
    x,y = map(int,input().split(' '))
    graph[x].append(y)
    graph[y].append(x)

def bfs(v):
    bacon = [0]* (n+1)
    queue = deque([v])
    visited[v] = True

    while (queue):
        k = queue.popleft()
        for i in graph[k]:
            if not visited[i]:
                bacon[i] = bacon[k] + 1
                visited[i] = True
                queue.append(i)
    return sum(bacon)

result = []
for i in range(1,n+1):
    result.append(bfs(i))
    visited = [False] * (n+1)
    # print(result)

arr = []
for i in range(len(result)):
    if result[i] == min(result):
        arr.append(i+1)

print(min(arr))

# ============================

# 완벽한 방법은 아니지만 답은 맞음

import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split(' '))
graph = [[] for x in range(n+1)]
for _ in range(m):
    x, y = map(int,input().split(' '))
    graph[x].append(y)
    graph[y].append(x)
# print(graph)

def bfs(v):
    visited = [0]*(n+1)
    queue = deque([v])
    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if visited[i] == 0:
                visited[i] = visited[a]+1
                queue.append(i)
    
    return(sum(visited))





result=[]
for i in range(1,n+1):
    result.append(bfs(i))
# print(result)
arr = []
for i in range(len(result)):
    if result[i] == min(result):
        arr.append(i+1)
print(min(arr))