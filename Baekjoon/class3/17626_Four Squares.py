# DP => 다이나믹 프로그래밍(동적 계획법)
# 하나의 문제는 단 한번만 풀도록 하는 알고리즘
# 1번 가정. 큰 문제를 작은 문제로 나눌 수 있다.
# 2번 가정. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.


import sys
n = int(sys.stdin.readline())

def four_squares(num):  
  if int(num**0.5) == num**0.5: # 25
    return 1

  for i in range(1, int(num**0.5)+1):  # 40 = 6^2 + 2^2(1~6) => i의 제곱과 num-i의 제곱으로 이루어져 있으니까
    if int((num - i**2)**0.5) == (num - i**2)**0.5:
      return 2

  for i in range(1, int(num**0.5)+1): # 41 = 6^2 + 2^2 + 1^1
    for j in range(1, int((num-i**2)**0.5)+1):
      if int((num - i**2 -j**2)**0.5) == (num - i**2 -j**2)**0.5:
        return 3
  return 4

print(four_squares(n))



# #잘못된 풀이
# import sys
# input = sys.stdin.readline
# n = int(input())
# if (int(n**0.5)**2 == n):
#     print(1)
# else:
#     m = n - int(n**0.5)**2
#     print(m)
#     if (int(m**0.5)**2 == m):
#         print(2)
#     else:
#         k = m - int(m**0.5)**2
#         print(k)
#         if (int(k**0.5)**2 == k):
#             print(3)
#         else:
#             print(4)
        


