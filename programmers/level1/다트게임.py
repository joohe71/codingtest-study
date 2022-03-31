# 다른 풀이
def solution(dartResult):
    stack = []
    dartResult = dartResult.replace('10', 'a')
    score = {'S':1, 'D':2, 'T':3}

    for i in dartResult:
        if i.isdigit() or i == 'a':
            stack.append(10 if i == 'a' else int(i))
            
        if i in ('S', 'D', 'T'):
            num = stack.pop()
            stack.append(num ** score[i])
            
        if i == '#':
            stack[-1] = stack[-1] * -1
            
        if i == '*':
            num = stack.pop()
            if len(stack):
                stack[-1] = stack[-1] * 2
            stack.append(num * 2)
            
    return sum(stack)