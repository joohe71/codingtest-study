def solution(n):
    answer = ''
    while n>0:
        p,r = divmod(n,3)
        if r == 0:
            r = 3
            n = p-1
            answer += "4"
        else:
            answer += str(r)
            n = p
    return answer[::-1]

# =========================
# 다른 풀이
def solution(n):
    answer = ''
    nums = [1,2,4]
    
    while n > 0:
        n -= 1
        answer += str(nums[n%3])
        n = n // 3
    return answer[::-1]