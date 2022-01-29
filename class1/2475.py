#입력
a = input().split()
sum = 0
for i in range(len(a)):
    b = int(a[i])**2
    sum = b + sum

#출력
print(sum%10)
