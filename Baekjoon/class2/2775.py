t = int(input())
count = 0
n_list = []
k_list = []
make = 0
for i in range(t):
    k = int(input()) #층(높이)
    n = int(input()) #호(가로)
    floor = list(range(1,n+1))
    for j in range(k):
        for h in range(1,n):
            floor[h] += floor[h-1]
    print(floor[-1])           
          
