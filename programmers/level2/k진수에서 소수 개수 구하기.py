# 참고 : https://kimjingo.tistory.com/147?category=946327


def changer(n, k):
    change = ""
    while (n//k > 0):
        change += str(n%k)
        n = n//k
    change += str(n)
    return "".join(reversed(change))

# 소수 판별하는 함수
def is_prime_num(k):
    if k == 2 or k == 3: 
        return True  
    if k % 2 == 0 or k < 2: 
        return False  
    
    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    change = changer(n, k)
    
    for n in change.split("0"):
        # print(n)
        if n == "":
            continue
        if is_prime_num(int(n)):
            answer += 1
    return answer
    