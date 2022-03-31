# F => 한 눈금 앞으로
# B => 한 눈금 뒤로
# L => 왼쪽으로 90도 회전
# R => 오른쪽으로 90도 회전
# https://fre2-dom.tistory.com/384 참고

import sys
input = sys.stdin.readline

dx = [0,-1,0,1] # 북, 서, 남, 동 => x축 이동
dy = [1,0,-1,0] # 북, 서, 남, 동 => y축 이동


T = int(input())
for _ in range(T):
  direction = list(input().strip())
  sx, sy, lx, ly = 0, 0, 0, 0
  x, y = 0, 0
  go = 0 # 북:0, 서:1, 남:2, 동:3

  for i in direction:
    if i == "F":
      x += dx[go]
      y += dy[go]
    
    elif i == "B":
      x -= dx[go]
      y -= dy[go]
    
    elif i == "L":
      if go == 3:
        go = 0
      else:
        go += 1
    
    elif i == "R":
      if go == 0:
        go = 3
      else:
        go -= 1
    
    sx = min(sx,x)
    sy = min(sy,y)
    lx = max(lx,x)
    ly = max(ly,y)

  print(abs((lx-sx)*(ly-sy)))