import sys
input = sys.stdin.readline
from collections import deque
m,n,h = map(int,input().split(' '))
graph = []
queue = deque([])
for i in range(h):
    arr = []
    for j in range(n):
        arr.append(list(map(int,input().split(' '))))
        for k in range(m):
            if arr[j][k] == 1:
                queue.append([i,j,k])
    graph.append(arr)
# print(graph)

dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
while(queue):
    x,y,z = queue.popleft()

    for i in range(6):
        nx = x+dx[i]
        ny = y+dy[i]
        nz = z+dz[i]
        if 0<=nx<h and 0<=ny<n and 0<=nz<m and graph[nx][ny][nz]==0:
            queue.append([nx,ny,nz])
            graph[nx][ny][nz]= graph[x][y][z]+1  

res= 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit()
        res = max(res,max(j))
print(res-1)