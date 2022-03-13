# # 시간초과
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# arr_a = []
# arr_b = []
# intersection = []
# for _ in range(n):
#     a = input().rstrip() # 듣도 못한 사람
#     arr_a.append(a)
# for _ in range(m):
#     b = input().rstrip() # 보도 못한 사람
#     arr_b.append(b)
# # print(arr_a,arr_b)
# if (n<=m):
#     for i in arr_a:
#         if i in arr_b:
#             intersection.append(i)
#     intersection.sort()
#     print(len(intersection))
#     for k in intersection:
#         print(k)
# else:
#     for j in arr_b:
#         if j in arr_a:
#             intersection.append(j)
#     intersection.sort()
#     print(len(intersection))
#     for l in intersection:
#         print(l)
# -----------------------------------------------------------
# # 시간초과
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# dict = {}
# intersection = []
# for i in range(n):
#     a = input().rstrip() # 듣도 못한 사람
#     dict[i] = a
# for j in range(n,n+m):
#     b = input().rstrip() # 보도 못한 사람
#     dict[j] = b
# # print(dict)
# count = 0
# arr = []
# for k in range(len(dict)-1):
#     for l in range(k+1,len(dict)):
#         if dict[k] == dict[l]:
#             count += 1
#             arr.append(dict[k])
#             arr.sort()
# print(count)
# for r in arr:
#     print(r)
# ==============================================================

# set 자료형 사용하기 => 중복 허용하지 않는다, 순서가 없다(unordered)
# 교집합( '&' 연산자 또는 intersection 사용)
# 합집합( '|' 연산자 또는 union 사용)

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = set()
b = set()
for _ in range(n):
    a.add(input().rstrip()) # 듣도 못한 사람
for _ in range(m):
    b.add(input().rstrip()) # 보도 못한 사람

result = sorted(list(a & b))
print(len(result))
for i in result:
    print(i)