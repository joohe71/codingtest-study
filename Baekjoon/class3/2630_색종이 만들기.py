import sys
from collections import deque
input = sys.stdin.readline
arr = []
n = int(input())
for _ in range(n):
    arr.append(list(map(int,input().split(' '))))

result = []

def divide(x, y, N):
    value = arr[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if value != arr[i][j]:
                divide(x, y+N//2, N//2)
                divide(x+N//2, y, N//2)
                divide(x, y, N//2)
                divide(x+N//2, y+N//2, N//2)
                return # why?
    if value == 0:
        result.append(0)
    else:
        result.append(1)

divide(0,0,n)

print(result.count(0))
print(result.count(1))





# def bfs(graph,y,x):
#     queue = deque([(y,x)])
#     graph[y][x] = 2
#     while queue:
#         b, a = queue.popleft()
#         for i in range(4):
#             nx = a + dx[i]
#             ny = b + dy[i]
#             if nx<0 or nx>=n or ny<0 or ny>=n:
#                 continue
#             if graph[ny][nx] == 1:
#                 graph[ny][nx] = 2
#                 queue.append((ny,nx))


# def bfs2(graph,y,x):
#     queue = deque([(y,x)])
#     graph[y][x] = 3
#     while queue:
#         b, a = queue.popleft()
#         for i in range(4):
#             nx = a + dx[i]
#             ny = b + dy[i]
#             if nx<0 or nx>=n or ny<0 or ny>=n:
#                 continue
#             if graph[ny][nx] == 0:
#                 graph[ny][nx] = 3
#                 queue.append((ny,nx))




# n = int(input())
# graph = []
# dx = [1,-1,0,0]
# dy = [0,0,1,-1]
# cnt= 0 
# for _ in range(n):
#     graph.append(list(map(int,input().split(' '))))

# cnt=0 
# cnt2=1         
# for y in range(n):
#     for x in range(n):
#         if graph[y][x] == 1:
#             bfs(graph,y,x)
#             cnt += 1
#         if graph[y][x] == 0:
#             bfs2(graph,y,x)
#             cnt2 += 1 




# print(cnt)
# print(cnt2)
