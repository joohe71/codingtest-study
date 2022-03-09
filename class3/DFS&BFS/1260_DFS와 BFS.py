# import sys
# from collections import deque #BFS
# input = sys.stdin.readline

# n,m,v = map(int,input().split(" "))

# # 각 노드가 연결된 정보 표현
# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#     x,y= map(int,input().split())
#     graph[x].append(y)
#     graph[y].append(x)

# for i in range(len(graph)):
#     graph[i].sort()

# # 각 노드가 방문된 정보 표현
# visited = [False] * (n+1)

# def dfs(graph,v,visited):
#     visited[v] = True
#     print(v, end=" ")
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)


# def bfs(graph,v,visited):
#     queue = deque([v])
#     visited[v] = True
#     # 큐에서 하나의 원소를 뽑아 출력하기
#     while queue:
#         v1 = queue.popleft()
#         print(v1, end=' ')
#         # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
#         for i in graph[v1]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i]=True

# dfs(graph,v,visited)
# visited = [False] * (n+1)
# print()
# bfs(graph,v,visited)

# ========================================

# 복습

import sys
from collections import deque
input = sys.stdin.readline
n,m,v = map(int,input().split(' '))
graph = [[] for x in range(n+1)]
isVisited = [False]*(n+1)
result = []
def dfs(v):
    isVisited[v] = True
    # print(v,end=' ')
    result.append(v)
    for i in graph[v]:
        if isVisited[i] == False:
            dfs(i)
    return result

def bfs(v):
    queue =deque([v])
    isVisited[v] = True
    while queue:
        a = queue.popleft()
        result.append(a)
        for i in graph[a]:
            if not isVisited[i]:
                queue.append(i)
                isVisited[i]=True
    return result

for _ in range(m):
    x, y = map(int,input().split(' '))
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort()


print(*dfs(v))
isVisited = [False] * (n+1)
result = []
print(*bfs(v))


