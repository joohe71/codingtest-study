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

# # 다른 방법
# n = int(input())
# result = 0
# n_min = n - 9*len(str(n)) # 1-18까지는 음수가 나옴
# if n_min > 1:
#   n_min
# else:
#   n_min = 1

# for i in range(n_min,n+1):
#   i_sum = 0
#   for j in str(i):
#     i_sum += int(j)
  
#   result = i_sum + i
  
#   if result == n:
#     print(i)
#     break

#   if n == i:
#     print(0)
#     break