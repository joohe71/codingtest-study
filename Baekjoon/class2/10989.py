# # 메모리 초과
# # sort 함수를 쓰면 안된다.
# # append 함수를 사용하게 되면 메모리 재할당이 이루어져서 메모리르 효율적으로 사용 못한다.
# import sys

# n = int(input())
# li = []

# for _ in range(n):
#     num = int(sys.stdin.readline())
#     li.append(num)

# for i in sorted(li):
#     print(i)

import sys

n = int(sys.stdin.readline())
li = [0] * 10000

for _ in range(n):
    num = int(sys.stdin.readline())
    li[num-1] += 1 
for i in range(len(li)):
    if li[i] != 0:
        for _ in range(li[i]):
            print(i+1)