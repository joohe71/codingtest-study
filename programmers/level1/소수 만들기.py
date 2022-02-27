def is_prime(x):
    for i in range(2,int(x**(0.5))+1):
        if x % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    three_sum = []
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                three_sum.append(nums[i] + nums[j] +nums[k])
    for i in three_sum:
        if (is_prime(i)):
            answer += 1 

    return answer