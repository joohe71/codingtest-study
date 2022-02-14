import sys
input = sys.stdin.readline

num = int(input()) # 수행해야 하는 연산의 수

s = [] #비어있는 공집합

for _ in range(num):
    calc = list(input().split()) # ["add", "3"]
    operation = calc[0]
    # value = calc[1]
    if operation == "add":
        if int(calc[1]) not in s:
            s.append(int(calc[1]))
    elif operation == "remove":
        if int(calc[1]) in s:
            s.remove(int(calc[1]))
    elif operation == "check":
        if int(calc[1]) in s:
            print(1)
        else:
            print(0)
    elif operation == "toggle":
        if int(calc[1]) in s:
            s.remove(int(calc[1]))
        else:
            s.append(int(calc[1]))
    elif operation == "all":
        s = [j for j in range(1,21)] # 리스트에 str값으로 변환해서 받으면 시간이 더 오래걸림! 
    elif operation == "empty":
        s = []
    print(s)
        
