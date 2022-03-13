# # 시간초과
# import sys
# n = int(sys.stdin.readline())
# card = [str(x) for x in range(1,n+1)]
# num = "".join(card)
# while (len(num)>2):
#         num = num[2:] + num[1]
# print(num[1])

# # deque는 앞, 뒤 양쪽 방향에서 element를 추가하거나 제거할 수 있다.
from collections import deque

n = int(input())
q = deque([x for x in range(1, n+1)])

while len(q) != 1:
    q.popleft()
    q.append(q.popleft())
print(q.pop())