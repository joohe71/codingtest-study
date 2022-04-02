# 정답

import sys
import itertools
input = sys.stdin.readline
N = int(input()) # 물약의 종류

dict = {}
price_list = list(map(int,input().strip().split(' ')))


for i in range(N):
  p = int(input())
  if p == 0:
    dict[i] = []
    pass
  else:
    for _ in range(p):
      a, d = map(int,input().strip().split(' '))
      if i in dict:
        dict[i].append((a-1, d))
      else:
        dict[i] = [(a-1, d)]

new_dict= {x:[] for x in range(N)}
for i, j in dict.items():
  if not j:
    pass
  else:
    for num, discount in j:
      if price_list[num] - discount <= 0:
        new_dict[i].append((num,price_list[num]-1))
      else:
        new_dict[i].append((num,discount))

# 순열 사용
nPr = itertools.permutations(new_dict.items(),N)
# print(list(nPr))

answer = []
for i in list(nPr):
  result = 0
  new_price_list = [x for x in price_list]
  for key, values in i:
    result += new_price_list[key]
    if not values:
      pass
    else:
      for num, discount in values:
        new_price_list[num] -= discount
        if new_price_list[num] <=0:
          new_price_list[num] = 1 
  # print(result)
  answer.append(result)
print(min(answer))
