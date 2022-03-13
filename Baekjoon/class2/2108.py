# best 풀이 - 1
import sys
input = sys.stdin.readline

n = int(input())

arr = [int(input()) for _ in range(n)]

# 평균
print(round(sum(arr) / n))

# 중앙값
sorted_arr = sorted(arr)
print(sorted_arr[n//2])

# 최빈값
dic = {}
for i in arr:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1


sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

max_num = sorted_dic[0][1]  # 2
max_list = []

for i in sorted_dic:
    if(i[1] == max_num):
        max_list.append(i[0])


if len(max_list) >= 2:
    max_list.sort()
    print(max_list[1])
else:
    print(max_list[0])

# 범위
print(max(arr) - min(arr))


# best 풀이 - 2
import sys
input = sys.stdin.readline
N = int(input()) # 수의 개수 N은 홀수
n_list = []
n_dic = {}

for i in range(N):
  num = int(input())

  n_list.append(num)

  if num not in n_dic: # 빈도 추가
    n_dic[num] = 1
  else:
    n_dic[num] += 1

print(n_dic)

# 평균
mean = round(sum(n_list) / N) 

n_list.sort() # 오름차순 정렬

# 중앙값
median = n_list[N//2] 

# 최빈값
freq = sorted(n_dic.items(), key=lambda x:(-x[1], x[0]))

if len(freq) != 1 and freq[0][1] == freq[1][1]:
  mode = freq[1][0]
else:
  mode = freq[0][0]

# 범위
n_range = n_list[N-1] - n_list[0]  

print(f'{mean}\n{median}\n{mode}\n{n_range}')






# 내풀이
# import sys
# from collections import Counter
# # Counter는 사전(dict) 클래스의 하위 클래스로 리스트나 튜플에서 각 데이터가 등장한 횟수를 사전 형식으로 돌려준다.
# n = int(sys.stdin.readline())
# arr = []
# for _ in range(n):
#     num = int(sys.stdin.readline())
#     arr.append(num)
# arr.sort()

# print(round(sum(arr)/n)) # 평균
# print(arr[n//2]) # 중앙값

# cnt = Counter(arr)
# mode = cnt.most_common() #등장한 횟수를 내림차순 정렬
# if n == 1:
#     print(num)
# elif mode[0][1] == mode[1][1]:
#     print(mode[1][0]) #최빈값
# else:
#     print(mode[0][0]) #최빈값

# print(max(arr)-min(arr)) #범위

