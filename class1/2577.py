a = int(input())
b = int(input())
c = int(input())

double = a*b*c
list = list(str(double))

while (True):    
    for i in range(10):
        print(list.count(str(i)))
    break
