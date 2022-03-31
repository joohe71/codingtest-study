def solution(progresses, speeds):
    array = []
    for x in range(len(progresses)):
        need = (100-progresses[x])/speeds[x]
        if int(need) == need:
            array.append(int(need))
        else:
            array.append(int(need)+1)
    print(array)

    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            array[i+1] = array[i]
    
    set_array = []
    for i in array:
        if i not in set_array:
            set_array.append(i)
    
    answer = []
    for i in set_array:
        answer.append(array.count(i))
    return answer


# =====================================
# 다른 풀이
def solution(progresses, speeds):
    answer = []
    workday = 0
    completed = 0
    
    while progresses:
        # 앞일이 먼저 100% 이상 완성되면 if로 들어가서 completed가 증가
        if progresses[0] + (workday * speeds[0]) >= 100: 
            progresses.pop(0)
            speeds.pop(0)
            completed += 1
        else:
            # 100% 완성되지 못한 work를 만났을 때 기존에 completed가 있으면 넣기
            if completed > 0:
                answer.append(completed)
                completed = 0
            # 일한 날 증가
            workday += 1
    
    # 마지막은 progresses가 다 비워져서 이후 append 불가능해서 마지막 것까지 넣음 
    answer.append(completed)
        
    return answer