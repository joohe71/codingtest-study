# 테스트 2개 시간초과
def solution(numbers):
    answer = []
    for num in numbers:
        binary = format(num,'b')
        next_num = num
        while True:
            cnt = 0
            next_num += 1
            bin_next = format(next_num,'b')
            if len(bin_next) != len(binary):
                binary = '0'*(len(bin_next)-len(binary)) + binary
            cnt += list(zip(format(next_num,'b'),binary)).count(('0','1')) 
            cnt += list(zip(format(next_num,'b'),binary)).count(('1','0'))
            if cnt <=2:
                answer.append(next_num)
                break
    return answer     