import sys
input = sys.stdin.readline

n = int(input())

stack = []
for _ in range(n):
    s = list(input().split())

    if (s[0] == "push"):
        stack.append(int(s[1]))
    elif (s[0] == "pop"):
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif (s[0] == 'size'):
        print(len(stack))
    elif (s[0] == 'empty'):
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])


