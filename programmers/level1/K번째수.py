def solution(array, commands):
    answer = []
    for i in commands:
        slicing = array[i[0]-1:i[1]] # 슬라이스
        slicing.sort() # 정렬
        answer.append(slicing[i[2]-1])
    
    return answer