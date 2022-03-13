# 참고: https://suri78.tistory.com/26

# 정렬 필요
# 1) 끝나는 시간 오름차순
# 2) 만약, 끝나는 시간이 같다면 시작 시간 순으로 오름차순

import sys
input = sys.stdin.readline
n = int(input())
dict = {}

for i in range(n):
    value = tuple(map(int,input().split()))
    dict[i] = value

value_list = sorted(dict.values(),key =lambda x:(x[1],x[0]))

end = value_list[0][1]
result = 1

for i in range(1,len(value_list)):
    if value_list[i][0] >= end:
        result +=1
        end = value_list[i][1]

print(result)