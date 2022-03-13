import sys
n = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
li = []
add = 0

# 소수이면 1, 아니면 0
for i in num:
    if i == 1:
        li.append(0)
    elif i == 2:
        li.append(1)
    else:
        for j in range(2,i):
            if i % j == 0:
                add = 1
                break
            else:
                add = 0
        # print(str(i)+"를"+str(j)+"로 나누었을 때", add)
        if add > 0:
            li.append(0)
        else:
            li.append(1)
print(sum(li))


            


