n = int(input()) #분해합

# 분해합>= 생성자
for i in range(1,n+1):
    num = sum(list(map(int,str(i))))
    num_sum = num + i
    if num_sum == n:
        print(i)
        break
    elif n == i:
        print(0)
