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