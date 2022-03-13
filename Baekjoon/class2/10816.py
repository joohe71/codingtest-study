# # 시간초과
# import sys
# input = sys.stdin.readline

# n = int(input())
# n_list = list(map(int,input().split()))
# m = int(input())
# m_list = list(map(int,input().split()))

# dic= {}

# for i in m_list:
#     dic[i] = 0 #초깃값 0
#     for j in range(len(n_list)):
#         if i == n_list[j]:
#             dic[i] += 1

# for r in dic.values():
#     print(r,end=" ")



# Counter 함수는 리스트를 값으로 주면 해당 원소들이 몇 번 등장했는지 세어 딕셔너리 형태로 반환 
from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int,input().split()))
m = int(input())
m_list = list(map(int,input().split()))

count = Counter(n_list) # Counter({10: 3, 3: 2, -10: 2, 6: 1, 2: 1, 7: 1})


for i in m_list:
    if count[i] :
        print(count[i],end= " ")
    else:
        print(0,end= " ")