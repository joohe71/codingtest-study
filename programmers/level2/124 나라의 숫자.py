def solution(n):
    answer = ''
    while n>0:
        p,r = divmod(n,3)
        if r == 0:
            r = 3
            n = p-1
            answer += "4"
        else:
            answer += str(r)
            n = p
    return answer[::-1]