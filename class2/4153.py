from cgi import test


while (True):
    test = list(map(int, input().split()))
    test.sort()
    a,b,c = test[0], test[1], test[2]
    if (a == 0 and b == 0 and c == 0):
        break
    if (a**2 + b**2 == c**2):
        print("right")
    else:
        print("wrong")

