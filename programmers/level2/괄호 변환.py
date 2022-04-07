# 문자열 p를 u,v로 분리하는 함수
def divide(p):
    left = 0
    right = 0
    
    for i in range(len(p)):
        if p[i] == "(":
            left += 1
        else:
            right += 1
        if left == right:
            u = p[:i+1]
            v = p[i+1:]
            return u, v

# 문자열 u가 올바른 괄호 문자열인지 확인하는 함수
def check(u):
    stack = []
    answer = ''
    
    for i in u:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                return False
            else:
                stack.pop()
    return True
            
        
def solution(p):
    if len(p) == 0: # 1
        answer = p
    else:
        u, v = divide(p) # 2
        
        if check(u): # 3
            return u + solution(v) # 3-1
        else:
            answer = "(" # 4-1
            answer += solution(v) # 4-2
            answer += ")" # 4-3
            
            for p in u[1:len(u)-1]: # 4-4
                if p == "(":
                    answer += ")"
                else:
                    answer += "("
    return answer