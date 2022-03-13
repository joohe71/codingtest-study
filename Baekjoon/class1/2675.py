T = int(input())
for i in range(T):
    R, S = input().split()
    R = int(R)
    a = list(S)
    for j in range(len(S)):
        a[j] = a[j]*R
    print("".join(a))
