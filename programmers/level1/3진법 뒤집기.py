def solution(n):
    result = ''
    
    while n > 0:
        p,r = divmod(n,3)
        result += str(r)
        n = p
        
    return int(result,3) #: 진법으로 구성된 str 형식의 수를 10진법으로 변환

