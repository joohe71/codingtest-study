import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    s = input()
    arr = [] #위치 주의

    for i in s:
        if i =="(" : #열린 괄호가 나오면 append
            arr.append(i)
        elif i == ")":
            if arr and arr[-1] == "(": 
                arr.pop()
            else:
                arr.append(i)
    print(arr)


    if len(arr) == 0: #짝이 맞는다면 빈 배열이므로
        print("YES")
    else:
        print("NO")