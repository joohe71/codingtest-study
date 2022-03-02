import sys
from collections import deque
input = sys.stdin.readline
t = int(input()) # 테스트의 개수



def bfs(graph,y,x):
    queue = deque([(y,x)])
    graph[y][x] = 0
    while queue:
        b, a = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append((ny,nx))



for i in range(t):
    m,n,k = map(int,input().split(' ')) #가로,세로,배추위치개수
    graph=[[0]*m for _ in range(n)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for _ in range(k):
        x,y = map(int,input().split(' '))
        graph[y][x] = 1
    

    cnt= 0            
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1:
                bfs(graph,y,x)
                #확인용
                # for i in graph:
                #     print(*i)
                # print('----------------------')
                cnt += 1
    
    print(cnt)