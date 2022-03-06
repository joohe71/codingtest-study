def solution(lottos, win_nums): # (민호's 로또번호 배열,당첨 번호를 담은 배열)
    zero_count= 0
    same_arr =[]
    answer=[]
    rank = {0:6, # 당첨 갯수 : 순위
            1:6,
            2:5,
            3:4,
            4:3,
            5:2,
            6:1}

            
    for i in win_nums:
        for j in lottos:
            if i == j:
                same_arr.append(i)

    for i in lottos:
        if i == 0:
            zero_count += 1
        
    answer.append(rank[len(same_arr)+zero_count])
    answer.append(rank[len(same_arr)])
    return answer

print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))