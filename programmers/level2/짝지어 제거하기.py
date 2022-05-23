# 스택
def solution(s):
    string = list(s)
    q = []
    for i in string:
        if not q:
            q.append(i)
        elif q[-1]==i:
            q.pop(-1)
        else:
            q.append(i)
    
    if len(q) == 0:
        return 1
    else:
        return 0