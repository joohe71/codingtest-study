num = list(map(int,input().split())) #정렬해주기 위해 리스트로 입력받기
num.sort()
a = num[0]
b = num[1]
max_li = []
min_li = []
for i in range(1,a+1):
    if a % i == 0 and b % i == 0:
        max_li.append(i)

max_value = max(max_li)            
min_value = int(max_value * (a / max_value) * (b / max_value))
print(max_value,min_value,sep='\n')    