list = []
while (True):
    for i in range(9):
        A = int(input())
        list.append(A)
    print(max(list))
    print(list.index(max(list))+1)
    break