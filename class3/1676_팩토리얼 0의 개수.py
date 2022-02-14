import sys
input = sys.stdin.readline
n = int(input())
fac = 1

#팩토리얼 구현
for i in range(2,n+1):
    fac *= i


arr = list(map(int,str(fac))) # [3,4,5,6,0,0]
count = 0 
# print(arr)
for j in reversed(range(len(arr))): #인덱스 거꾸로 확인 => 0의 연속 개수 확인
    if arr[j] == 0:
        count += 1
    else:
        break
print(count)
