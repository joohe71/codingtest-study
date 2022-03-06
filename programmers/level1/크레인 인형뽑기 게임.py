def solution(board, moves):
    dict = {}
    answer = 0
    box = [0]
    arr = [[] for x in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board)):
            arr[j].append(board[i][j]) 
    
    # for i in range(1,len(board)+1):
    #     dict[i] = arr[i-1]        

    for i in moves:
        if arr[i-1] != [0 for x in range(len(board))]:
            for j in range(len(board)):
                if arr[i-1][j] != 0:
                    if box[-1] == arr[i-1][j]:
                        del box[-1]
                        # 틀린 이유 아래 코드 안넣어줘서...
                        arr[i-1][j] = 0
                        answer += 1
                    else:
                        box.append(arr[i-1][j])
                        arr[i-1][j] = 0
                    break

    return answer*2

# ===========================================
