import sys
input = sys.stdin.readline
num = int(input()) # 컴퓨터의 수
connect = int(input())
network=[[] for _ in range(num+1)] #각 컴퓨터에 연결된 정보 표현
for _ in range(connect):
    x, y = map(int,input().split(' '))
    network[x].append(y)
    network[y].append(x)

for i in range(1,len(network)):
    network[i].sort()
virus = [False] * (num+1)

def dfs(v):
    virus[v] =True
    for i in network[v]:
        if not virus[i]:
            dfs(i)
    return virus.count(True)-1

print(dfs(1))