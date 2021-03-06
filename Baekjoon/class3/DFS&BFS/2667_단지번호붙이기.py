# import sys
# input = sys.stdin.readline
from collections import deque
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs(y,x):
    cnt = 1
    queue = deque([(y,x)])
    graph[y][x] = 0 # 방문했으니까 0으로 바꾸기
    while queue:
        b,a = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0 # 방문했으니까 0으로 바꾸기
                queue.append((ny,nx))
                cnt +=1
    return cnt

result = []
for i in range(len(graph)):
    for j in range(len(graph)):
        if graph[j][i] == 1:
            result.append(bfs(j,i))

result.sort()
print(len(result))
for i in result:
    print(i)

# ===========================================

# 복습


import sys
from collections import deque
input = sys.stdin.readline
n= int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().rstrip())))
# print(graph)

dx = [1,-1,0,0]
dy = [0,0,1,-1]
count = 0
def bfs(x,y):
    queue=deque([[x,y]])
    graph[x][y] = 0
    count = 1
    while queue:
        nx,ny = queue.popleft()
        for i in range(4):
            a = nx + dx[i]
            b = ny + dy[i]
            if 0<=a<n and 0<=b<n:
                if graph[a][b]==1:
                    count += 1
                    graph[a][b] = 0
                    queue.append([a,b]) 
    return count

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(i,j))

print(len(result))
result.sort()
for i in result:
    print(i)

