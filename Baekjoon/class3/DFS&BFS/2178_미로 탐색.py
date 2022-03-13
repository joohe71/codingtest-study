from collections import deque
n,m = map(int,input().split(' '))
graph = []

for _ in range(n):
    graph.append(list(map(int,input())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(y,x):
    # 데크 생성
    queue = deque([(y,x)])
    while queue:
        b,a = queue.popleft()
        # 4가지 방향 위치 확인
        for i in range(4):
            nx = dx[i]+a
            ny = dy[i]+b
            # 위치가 벗어나면 안되기 때문에 조건 추가
            if nx<0 or nx>=m or ny>=n or ny<0:
                continue
            # 벽이므로 진행 불가
            if graph[ny][nx] == 0:
                continue
            # 벽이 아니므로 이동
            if graph[ny][nx] == 1:
                graph[ny][nx] = graph[b][a]+1
                queue.append((ny,nx))
    
    # 마지막 값 출력
    return graph[n-1][m-1]

print(bfs(0,0))          


# ========================================

# 븍습

import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int,input().split(' '))
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().rstrip())))
# print(graph)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    queue=deque([[x,y]])
    while queue:
        nx,ny = queue.popleft()
        for i in range(4):
            a = nx + dx[i]
            b = ny + dy[i]
            if 0<=a<n and 0<=b<m:
                if graph[a][b]==1:
                    graph[a][b]=graph[nx][ny]+1
                    queue.append([a,b]) 
    return(graph[n-1][m-1])

print(bfs(0,0))

