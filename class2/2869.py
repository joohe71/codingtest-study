# 답은 맞지만 시간 초과
# a, b, v = map(int,input().split())
# i = 1
# start = 0
# while (1==1):
#     start += a
#     if start >= v:
#         print(i)
#         break
#     else:
#         start -= b
#         i += 1


a, b, v = map(int,input().split())
day = (v - b) / (a - b)
if day != int(day):
    print(int(day)+1)
else:
    print(int(day))


