# # 시간초과
# import sys
# ex_num = int(sys.stdin.readline())
# ex = list(map(int,sys.stdin.readline().split()))
# sol_num = int(sys.stdin.readline())
# sol = list(map(int,sys.stdin.readline().split()))
# for i in sol:
#     if i in ex:
#         print(1)
#     else:
#         print(0)


# # 탐색과 확인이 주로 필요하면 set이나 dictionary
# # 순서와 index에 따른 접근이 필요하면 list
 
import sys
ex_num = int(sys.stdin.readline())
ex = list(map(int,sys.stdin.readline().split()))
ex.sort() #이진 탐색을 하기 위해서는 자료 정렬 필요
sol_num = int(sys.stdin.readline())
sol = list(map(int,sys.stdin.readline().split()))

# 이진 탐색 알고리즘
def binary_search(ex_list, x):
    start = 0
    end = len(ex_list) - 1

    while start <= end:
        mid = (start + end) // 2
        if x == ex_list[mid]:
            return 1
        elif x > ex_list[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for i in sol:
    print(binary_search(ex,i))


# 다른풀이
# n = int(input())
# n_list = list(map(int, input().split()))
# m = int(input())
# m_list = list(map(int, input().split()))
# n_dic = {}

# for i in n_list:
#   if i not in n_dic:
#     n_dic[i] = 1
#   else:
#     n_dic[i] += 1
    
# print(n_dic)
# for j in m_list:
#   if j not in n_dic.keys(): # n_dic.keys()
#     print("0")
#   else:
#     print("1")