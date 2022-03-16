def solution(x):
    arr = list(map(int,str(x)))
    if x % sum(arr) == 0:
        answer = True
    else:
        answer = False
    return answer