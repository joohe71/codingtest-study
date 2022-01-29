#입력
A = []
for i in range(10):
    B = int(input())%42
    A.append(B)

# 출력
new_list = []
for i in range(10):
    if (A[i] not in new_list):
        new_list.append(A[i])

print(len(new_list))


