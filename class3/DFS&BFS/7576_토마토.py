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
     


# ==================================


from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n = map(int, input().split())
n_list = [list(map(int, input().split())) for _ in range(n)]

que = deque()
for i in range(n):
  for j in range(m):
    if n_list[i][j] == 1:
      que.append((i,j,0))

while que:
  tx, ty, tday = que.popleft()
  for i in range(4):
    nx = dx[i] + tx
    ny = dy[i] + ty
    nday = tday + 1

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
      continue

    if n_list[nx][ny] == 0:
      que.append((nx,ny,nday))
      n_list[nx][ny] = 1
    
print(tday)
print(n_list)

for i in range(n):
  if n_list[i].count(0) > 0:
    tday = -1
    break

print(tday)

