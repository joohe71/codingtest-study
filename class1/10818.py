num1 = int(input())
num2 = list(map(int,input().split()))
# print(min(num2), max(num2))

num2.sort()
print(num2[0],num2[-1])
