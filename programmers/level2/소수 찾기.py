from itertools import permutations

def solution(numbers):
    arr = []
    for i in range(1,len(numbers)+1):
        for j in permutations(numbers,i):
            string = "".join(j)
            if string not in arr:
                arr.append(string)
    
    result = []
    for i in arr:
        if int(i) in [0,1]:
            pass
        else:
            for j in range(2,int(i)):
                if int(i) % j == 0:
                    break
            else:
                result.append(i)    
                

    cnt = 0            
    for i in result:
        if str(int(i)) == i:
            cnt += 1
    return cnt