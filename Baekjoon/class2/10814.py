import sys


n = int(input())

dict = {}
for i in range(n):
    age, name = sys.stdin.readline().split()
    age = int(age)
    dict[i+1] = [age,name]
a = sorted(dict.items(), key = lambda x: (x[1][0],x[0]))

for i in range(len(a)):
    print(a[i][1][0], a[i][1][1], sep =" ")
