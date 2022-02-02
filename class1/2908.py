a, b = input().split()
a= int(''.join(reversed(a)))
b = int(''.join(reversed(b)))
if a >= b :
    print(a)
else :
    print(b)

# 다른코드1
# a, b = input().split()
# reversed_a = ''
# reversed_b=''
# for i in range(len(a)-1, -1, -1):
#   reversed_a +=a[i]
# for i in range(len(b)-1, -1, -1):
#   reversed_b +=b[i]

# print(max(int(reversed_a), int(reversed_b)))

# 다른코드2
# a, b = input().split()  # 2908

# a_reverse = a[::-1] # reverse
# b_reverse = b[::-1]

# if a_reverse > b_reverse :
#   print(a_reverse)
# else:
#   print(b_reverse)