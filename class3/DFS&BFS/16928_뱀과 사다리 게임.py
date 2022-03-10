import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int,input().split(' ')) # 사다리의 수, 뱀의 수
graph = [[] for _ in range(101)]
visited = [False] * 101
result = [0 for _ in range(101)]

# 사다리
for _ in range(n):
    x, y = map(int,input().split(' '))
    graph[x].append(y)

# 뱀
for _ in range(m):
    u, v = map(int,input().split(' '))
    graph[u].append(v)


def bfs(v):
    queue = deque([v])
    visited[v] =True
    while(queue):
        x = queue.popleft()
        if x == 100:
            print(result[x])
            break
        else:
            for move in range(1,7):
                nx = x + move
                if 0< nx <= 100 and not visited[nx]:
                    

                    if not graph[nx]:
                        visited[nx] =True
                        result[nx] = result[x] + 1
                        queue.append(nx)    
                    else:
                        nx1 = graph[nx][0]
                        if not visited[nx1]:
                            visited[nx1] = True
                            result[nx1] = result[x]+1
                            queue.append(nx1)
            # print(queue)
            # print('========================')
            # print(result)
bfs(1)


