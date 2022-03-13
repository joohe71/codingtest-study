# 브루트 포스 알고리즘 : 단순무식한 알고리즘 -> 시간측면에서 매우 비효율적이지만 만들기 쉬운편
# 참고 자료 => https://god-gil.tistory.com/62 
# # 다른 사람 풀이
# n, m = map(int, input().split())
# board = []
# for _ in range(n):
#   BW = list(input())
#   board.append(BW)

# result = []
# for i in range(n-7): # 세로
#   for j in range(m-7): # 가로
#     cnt_w=0 # 처음이 w 시작일 때
#     cnt_b=0 # 처음이 b 시작일 때
#     for x in range(i, i+8):
#       for y in range(j, j+8):
#         if (x+y)%2 == 0:
#           if board[x][y] != 'W': # 짝수자리가 B라면
#             cnt_w +=1 # 짝수자리를 w 로 바꿔줘야하므로 +1
#           else:
#             cnt_b +=1 # 짝수자리가 w라면 b로 바꿔줘야하므로 +1
#         else:
#           if board[x][y] != 'B':
#             cnt_w+=1
#           else:
#             cnt_b+=1
#     result.append(cnt_w)
#     result.append(cnt_b)
# print(min(result)) # 답