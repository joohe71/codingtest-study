# 중복이 없다
# 여벌의 체육복이 있는 학생도 도난 당했을 수 있다.
# 그리디 알고리즘
def solution(n, lost, reserve):
    set_lost  = set(lost)-set(reserve)
    set_reserve = set(reserve)-set(lost)
    for i in set_reserve:
            if i-1 in set_lost:
                set_lost.remove(i-1)
            elif i+1 in set_lost:
                set_lost.remove(i+1)
                
        
    answer = n-len(set_lost)
    return answer