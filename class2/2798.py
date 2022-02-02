from itertools import combinations #조합 사용하기

n, m = map(int,input().split()) #카드의 개수, 숫자
num = list(map(int,input().split()))
my_list = list(combinations(num,3))

t = []
for i in range(len(my_list)):
    my_sum = sum(my_list[i])
    if my_sum <= m:
        t.append(my_sum)
print(max(t))

