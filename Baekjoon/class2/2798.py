from itertools import combinations #조합 사용하기

n, m = map(int,input().split()) #카드의 개수, 숫자
num = list(map(int,input().split()))
my_list = list(combinations(num,3))

t = []
for i in range(len(my_list)):
    my_sum = sum(my_list[i])
    if my_sum <= m:
        t.append(my_sum)
print(max(t))

# # 다른풀이 1
# from itertools import combinations

# n ,m = map(int, input().split())
# cards = list(map(int, input().split()))

# data = list(combinations(cards,3))

# result = {}
# for i in data:
#   if sum(i)<=m:
#     result[sum(i)] = abs(sum(i)-m)
#   else:
#     continue
# print(result)
# print(min(result, key = result.get))

# # 다른풀이 2
# n,m = map(int,input().split())
# n_list = list(map(int, input().split()))
# n_max = -1
# for i in range(n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             if n_list[i] + n_list[j] + n_list[k] <= m:
#                 n_max = max(n_max, n_list[i] + n_list[j] + n_list[k])
# print(n_max)
