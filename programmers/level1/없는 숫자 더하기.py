def solution(numbers):
    answer = 0
    arr = [x for x in range(0,10)]
    for i in arr:
        if i not in numbers:
            answer += i

    return answer