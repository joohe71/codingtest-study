# 참고 : https://dev-note-97.tistory.com/128
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order), c)
            temp += combi
            # print(temp)
        counter = Counter(temp)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)


# from itertools import combinations
# from collections import Counter

# def menu(orders, course):
#     answer = []
#     combi = []
#     length = []
#     for i in orders:
#         length.append(len(i))
        
#     for i in orders:
#         if max(length) < course:
#             return False
#         for j in combinations(sorted(i),course): # sorted(str) => return type이 list이다.
#             combi.append("".join(j))

#     counter_result = Counter(combi).most_common()
#     max_num = counter_result[0][1]
#     print(counter_result)
#     print(max_num)
#     for i, j in counter_result:
#         if j == max_num and j > 1:
#             answer.append(i)
#     return answer

# def solution(orders, course):
#     answer = []
#     for num in course:
#         if not menu(orders, num):
#             pass
#         else:
#             for i in menu(orders, num):
#                 answer.append(i)
#     answer.sort()
#     return answer