import sys
input = sys.stdin.readline
num, money = map(int, (input().split(' ')))
coin = []
result=0
for _ in range(num):
    m = int(input())
    coin.append(m)
coin.sort(reverse=True)

for i in coin:
    if money == 0:
        break
    result += money//i
    money %= i # 나머지
print(result)