def solution(n):
    arr = []
    for i in range(n+1):
        if i == 0:
            arr.append(0)
        elif i == 1:
            arr.append(1)
        else:
            arr.append(arr[i-1] + arr[i-2])
    
    return arr[-1] % 1234567


# 안좋은 코드
# def solution(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         answer = solution(n-1) + solution(n-2)
#         return answer % 1234567