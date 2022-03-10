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

