# 더 쉬운 풀이
def solution(sizes):
    w = []
    h = []
    for i in sizes:
        i.sort()
        w.append(i[0])
        h.append(i[1])
    return max(w) * max(h)

# ==================================

def solution(sizes):
    width = []
    height = []
    for i in sizes:
        i.sort()
        width.append(i[0])
        height.append(i[1])
    width.sort()
    height.sort()
        
    answer = max(width) * max(height)
    return answer