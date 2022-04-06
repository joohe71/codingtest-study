from itertools import combinations

def each(place1):
    person = [] 
    for i in range(5):
        for j in range(5):
            if place1[i][j] == "P":
                person.append((i,j)) 
                
    combi = list(combinations(person,2))
        
    problem = [] # 맨하튼 거리 지켜지지 않은 좌표쌍들의 리스트
    
    for i,j in combi:
        if abs(i[0]-j[0]) + abs(i[1]-j[1]) <= 2:
            problem.append((i,j))
    
    cnt = 0
    for i,j in problem:
        
        # 붙어 있을 경우
        if abs(i[0]-j[0]) + abs(i[1]-j[1]) == 1:
            cnt += 1
            
        else:
            # 거리가 2이고 사이에 빈칸이 있을 경우
            if (i[0]+j[0])/2 == (i[0]+j[0])//2 and (i[1]+j[1])/2 == (i[1]+j[1])//2:
                if place1[(i[0]+j[0])//2][(i[1]+j[1])//2] == "X":
                    continue
                else:
                    cnt += 1
            # 대각선의 경우 모두 따져 주기 => x,y좌표가 모두 같을 경우까지!!
            if (i[0] == j[0]+1 and i[1] == j[1]-1) or (i[0] == j[0]-1 and i[1] == j[1]+1) or (i[0] == j[0]-1 and i[1] == j[1]-1):
                if place1[i[0]][j[1]] == "X" and place1[j[0]][i[1]] == "X":
                    continue
                else:
                    cnt += 1
                
    
    if cnt == 0:
        return 1
    else:
        return 0

    
def solution(places):
    answer = []
    
    for i in places:
        answer.append(each(i))
        
    return answer