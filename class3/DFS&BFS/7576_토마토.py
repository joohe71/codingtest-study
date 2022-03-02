import sys
input = sys.stdin.readline
from collections import deque
box = []
m,n = map(int,input().split(' ')) # 가로, 세로

for _ in range(n):
    box.append(list(map(int,input().split(' '))))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
res = 0

queue = deque([])

for i in range(m):
    for j in range(n):
        if box[j][i] == 1:
            queue.append((j,i))


def bfs(box):    
    while queue:
        b, a = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            if box[ny][nx] == 0:
                box[ny][nx] = box[b][a]+1
                queue.append((ny,nx))
        # for b in box:
        #     print(*b)
        # print('=================') 


bfs(box)

for i in box:
    for j in i:
        if j == 0:
            print(-1)
            exit() #프로그램 강제 종료
    
    res = max(res,max(i))

print(res-1)       
     





