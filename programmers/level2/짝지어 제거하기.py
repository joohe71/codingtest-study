# 큐
def solution(s):
    string = list(s)
    q = []
    for i in range(len(string)):
        if not q:
            q.append(string[i])
        elif q[-1]==string[i]:
            q.pop(-1)
        else:
            q.append(string[i])
    
    if len(q) == 0:
        return 1
    else:
        return 0