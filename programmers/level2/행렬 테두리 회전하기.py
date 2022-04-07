# 다른 사람 풀이(복습)
def solution(rows, columns, queries):
    answer = []
    board = [[0 for _ in range(columns+1)] for _ in range(rows+1)]
    start = 1
    
    for i in range(1,rows+1):
        for j in range(1, columns+1):
            board[i][j] = start
            start += 1
    
    for x1, y1, x2, y2 in queries:
        temp = board[x1][y1]
        min_num = temp
        
        # top 방향
        for i in range(x1, x2):
            new = board[i+1][y1]
            board[i][y1] = new
            min_num = min(min_num, new)
        
        # right 방향
        for i in range(y1,y2):
            new = board[x2][i+1]
            board[x2][i] = new
            min_num = min(min_num, new)
            
        # bottom 방향
        for i in range(x2,x1,-1):
            new = board[i-1][y2]
            board[i][y2] = new
            min_num = min(min_num, new)
        
        # left 방향
        for i in range(y2,y1, -1):
            new = board[x1][i-1]
            board[x1][i] = new
            min_num = min(min_num, new)
        
        board[x1][y1+1] = temp
        answer.append(min_num)
    return answer
