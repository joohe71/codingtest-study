# # 시간 초과
# def solution(N, stages):
#     dict = {x:[] for x in range(1,N+1)}
#     answer = {x:0 for x in range(1,N+1)}
#     # print(dict)
#     for i in stages:
#         for j in list(dict.keys()):
#             if i > j:
#                 dict[j].append(i)
#     # print(dict)
#     answer[1]= (len(stages)-len(dict[1]))/len(stages)
#     # print(answer)  
    
#     for i in range(1,N):
#         success1 = len(dict[i])
#         if success1 == 0:
#             answer[i+1] = 0
#         else:
#             success2 = len(dict[i+1])
#             fail = success1-success2
#             answer[i+1]=(fail/success1)
            
#     result = sorted(answer, key=lambda x:answer[x], reverse=True)
    
    
#     # sol=[i[0] for i in result]
            
#     return result

def solution(N,stages):
    result = {}
    d = len(stages)
    for stage in range(1,N+1):
        if d != 0:
            count = stages.count(stage)
            result[stage]= count / d
            d -= count
        else:
            result[stage] = 0
    return sorted(result,key=lambda x:result[x], reverse=True)
