def solution(answers):
    result1 = []
    result2 = []
    result3 = []
    cnt = [0,0,0]
    
    for _ in range(len(answers)):
        for j in range(1,6):
            result1.append(j)
            
    for _ in range(len(answers)):
        for j in [1,3,4,5]:
            result2.append(2)
            result2.append(j)
            
    for _ in range(len(answers)):
        for i in [3,1,2,4,5]:
            result3.append(i)
            result3.append(i)
    
    # print(result1, result2, result3, sep="\n")
    
            
    for i in range(len(answers)):
        if result1[i] == answers[i]:
            cnt[0]+=1
        if result2[i] == answers[i]:
            cnt[1]+=1
        if result3[i] == answers[i]:
            cnt[2]+=1
            
    # print(cnt)    
    answer = []
    for i in range(len(cnt)):
        if max(cnt) == cnt[i]:
            answer.append(i+1)
    answer.sort()    
        
    return answer