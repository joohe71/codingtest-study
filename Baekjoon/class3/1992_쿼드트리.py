import sys
input = sys.stdin.readline
num = int(input())
image = []
for _ in range(num):
    image.append(list(map(int,input().rstrip()))) # x행 y열

def compression(x,y,n):

    check = image[x][y] # 첫번째 원소
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != image[i][j]: # 하나라도 다르면 4등분
                print('(',end='')
                compression(x,y,n//2) # 1사분면
                compression(x,y+n//2,n//2) # 2사분면
                compression(x+n//2,y,n//2) # 3사분면
                compression(x+n//2,y+n//2,n//2) # 4사분면
                print(')',end='')
                return
    if check == 0:
        print('0',end='')
        return
    else:
        print('1',end='')
        return

compression(0,0,num)
                

