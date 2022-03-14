def solution(n):
    result = ''
    
    while n > 0:
        p,r = divmod(n,3)
        result += str(r)
        n = p
        
    return int(result,3) #: 진법으로 구성된 str 형식의 수를 10진법으로 변환

# ====================
# 다른 방법
def solution(n):
    answer = 0
    result = ""
    real = 0
    while n > 0:
        rest = n%3
        n = n//3
        result += str(rest)
    print(result)
    
    for i in range(len(result)):
        real += (int(result[i]) * (3**(len(result)-i-1)))
    answer = real
    return answer