# 더 간결한 코드
def solution(absolutes, signs):
    answer = 0
    for index, num in enumerate(absolutes):
        answer += num if signs[index] else -num
    return answer


def solution(absolutes, signs):
    for i in range(len(signs)):
        if not signs[i] :
            absolutes[i] = -absolutes[i]
    answer = sum(absolutes)
            
    return answer