# arr1 : [[1, 2, 3], [4, 5, 6]]

# arr2 : [[1, 4], [2, 5], [3, 6]]

# return : [[14, 32], [32, 77]]

def solution(arr1, arr2):
    # 행렬 만들기
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    new_arr = [[] for i in range(len(arr2[0]))]
    
    for i in arr2:
        for j in range(len(i)): 
            if len(arr2[0]) < j:
                pass
            else:
                new_arr[j].append(i[j])
                
    # print(new_arr)
    
    for i in range(len(arr1)):
        for j in range(len(new_arr)):
            value = [a*b for a,b in zip(arr1[i],new_arr[j])]
            answer[i][j] = sum(value)
    # print(answer)
    return answer