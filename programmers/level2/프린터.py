from collections import deque
def solution(priorities, location):
    dict = {}
    answer = []
    for i, letter in enumerate(priorities):
        dict[i] = letter
    
    # print(dict)
    
    queue = deque(list(dict.items()))
    queue_values = list(dict.values())
    while queue:
        i, letter = queue.popleft()
    
        if letter < max(queue_values):
            queue.append((i,letter))
        else:
            answer.append(i)
            queue_values[i] = 0
    
    # print(answer)
    for i, j in enumerate(answer):
        if j == location:
            return i+1