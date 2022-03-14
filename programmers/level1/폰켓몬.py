def solution(nums):
    if len(set(nums))>len(nums)//2:
        return len(nums)//2
    else:
        return len(set(nums))
    

# ============================
# 다른 풀이
def solution(nums):
    answer = 0
    dic = {}
    n = len(nums)//2
    result = 0
    
    for i in set(nums):
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
            
    print(dic)
    print(len(dic))
    
    for key, values in dic.items():
        result += values
    
    if result >= n:
        answer = n
    else:
        answer = result
        
    return answer