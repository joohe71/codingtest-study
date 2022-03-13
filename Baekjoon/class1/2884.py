H, M = input().split()

H = int(H)
M = int(M)

if M >= 45:
    print(H, M-45)
else:
    if H == 0:
        print(23,M+15)
    else:
        print(H-1,M+15)

#다른 문제 풀이
# h, m = map(int,input().split())

# m = m - 45

# if(m < 0):
#     m = m + 60
#     h = h -1

# if(h < 0):
#     h = h + 24

# print(h, m)