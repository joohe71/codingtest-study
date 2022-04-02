# 정답 확인 못함 => 시간 안에 못품( 6분 초과 )

import sys
from itertools import product, combinations
input = sys.stdin.readline
N = int(input())
string = list(input().strip())
num_dict = {
  'W': 0,
  'H': 1,
  'E': 2,
}
dict = {}
result = []
for i in range(len(string)):
  if string[i] in num_dict:
    dict[i] = num_dict[string[i]]

sorted_dict = sorted(dict.items(),key=lambda x:x[1],)

zero = []
one = []
two = []


for i,j in sorted_dict:
  if j == 0:
    zero.append((i,j))
  elif j == 1:
    one.append((i,j))
  elif j == 2:
    two.append((i,j))

arr = [x for x in two]
for i in range(2,len(two)+1):
  nPr = list(combinations(two,i))
  for i in nPr:
    arr.append(i[0])

# print(arr)
  

available_list = []
for i in product(zero,one,two,arr):
  available_list.append(i) 

# print(available_list)

answer = 0
for i,j,k,l in available_list:
  if i[0] < j[0] < k[0] < l[0]:
    answer += 1

print(answer)