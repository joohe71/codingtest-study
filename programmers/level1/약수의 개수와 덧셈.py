def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)**2 == i:
            answer -= i
        else:
            answer += i
    return answer

# ===============================
# 딕셔너리 방법

# def solution(left, right):
#     answer = 0
#     dic = {}
    
#     for num in range(left, right+1):
#         count = 0
#         for i in range(1, int(num**0.5)+1):
#             if num%i == 0:
#                 if i*i == num:
#                     count += 1 
#                 else:
#                     count += 2
#         dic[num] = count
        
#     print(dic)
#     for key, values in dic.items():
#         if values%2 == 0:
#             answer += key
#         else:
#             answer -= key

#     return answer