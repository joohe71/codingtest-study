n , k = map(int, input().split())

# 이항계수
son = []
mom = []
for i in range(k):
    son.append(n)
    mom.append(i+1)
    n -= 1

def mul(a):
    value = 1
    for i in range(len(a)):
        value *= a[i]
    return value

print(int(mul(son)/mul(mom)))