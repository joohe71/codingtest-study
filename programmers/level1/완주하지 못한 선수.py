def solution(participant, completion): #(참여자,완주자)
    
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if completion[i] != participant[i]:
            return participant[i]
    return participant[-1] # 전부 다돌아도 없을 경우에는 마지막 주자가 완주하지 못한 선수이다.