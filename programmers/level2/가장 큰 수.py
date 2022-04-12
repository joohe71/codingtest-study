# 참고 : https://huidea.tistory.com/4

def solution(numbers):
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    
    numbers.sort(key=lambda x: x*3, reverse=True) 

    return str(int("".join(numbers)))


# # 시간초과
# from itertools import permutations
# def solution(numbers):
#     for i in range(len(numbers)):
#         numbers[i] = str(numbers[i])
#     print(numbers)
#     max_num = 0
#     for i in permutations(numbers,len(numbers)):
#         string = "".join(i)
#         max_num = max(int(string),max_num) 

#     return str(max_num)