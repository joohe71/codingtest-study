from itertools import permutations
def solution(k, dungeons):
    answer = 0
    for value in permutations(dungeons,len(dungeons)):
        # print(value)
        cnt = 0
        p = k
        for i in value:
            if i[0] <= p:
                p -= i[1]
                cnt += 1
                
        answer = max(answer,cnt)
        # print(answer)
    
    return answer