import sys
input = sys.stdin.readline

n = int(input())
switch = list(map(int,input().split(' ')))
m = int(input())
# arr =[]
for _ in range(m):
    a,b = map(int,input().split(' '))

    if a == 1: # 남학생
        for i in range(1,n+1):
            if (i) % b == 0:
                if switch[i-1]==0:
                    switch[i-1] = 1
                else:
                    switch[i-1] = 0
    else: # 여학생
        if b+1 > n or b-1 <1: # 예외처리
            if switch[b-1] ==0:
                switch[b-1] = 1
            else:
                switch[b-1] = 0
        else:
            if switch[b-2] == switch[b]:
                left = b-2
                right = b

                while 1:
                    if left < 1 or right+2 > n:
                        break
                    if switch[left-1] != switch[right+1]:
                        break
                    else:
                        left -= 1
                        right += 1
                for i in range(left,right+1):
                    if switch[i]==0:
                        switch[i] = 1
                    else:
                        switch[i] = 0

             


print(*switch)


