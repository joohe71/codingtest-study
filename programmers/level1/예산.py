# 참고
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)

# from itertools import combinations
# def solution(d, budget):
#     d.sort()
#     answer = 0
#     for i in range(len(d),0,-1):
#         for j in combinations(d,i):
#             if budget >= sum(j):
#                 if answer < sum(j):
#                     answer = len(j)
#                     break
                
            
#         if answer != 0:
#             break
        
            
#     return answer