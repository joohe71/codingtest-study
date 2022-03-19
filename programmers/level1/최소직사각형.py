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