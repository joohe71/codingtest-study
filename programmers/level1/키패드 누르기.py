# (순서대로 누를 번호가 담긴 배열, left or right)
# 참고 사이트 => https://life-of-panda.tistory.com/75

def solution(numbers, hand):
    for i in range(len(numbers)):
        if numbers[i] == 0:
           numbers[i] = 11 
    answer = ''
    l_status = 10
    r_status = 12
    for i in range(len(numbers)):
        if numbers[i] in [1,4,7]:
            answer += "L"
            l_status = numbers[i]
        elif numbers[i] in [3,6,9]:
            answer += "R"
            r_status = numbers[i]
        else:
            left_result = abs(numbers[i]-l_status)
            right_result = abs(numbers[i]-r_status)
            p1, r1 = divmod(left_result,3) 
            p2, r2 = divmod(right_result,3) 
            if (p1 + r1) != (p2 + r2):
                if (p1 + r1) > (p2 + r2): 
                    answer += "R"
                    r_status = numbers[i]
                else:
                    answer +="L"
                    l_status = numbers[i]
            else:
                if hand == "left":
                    answer += "L"
                    l_status = numbers[i]
                else:
                    answer += "R"
                    r_status = numbers[i]


    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))