import sys
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(tuple(map(int,sys.stdin.readline().split())))

for i in arr:
    rank = 1
    for j in arr:
        if i[0] < j[0] and i[1] <j[1]:
            rank += 1
    print(rank)
