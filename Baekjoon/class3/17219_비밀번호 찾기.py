import sys
input = sys.stdin.readline
n, m = map(int,input().split())
dict = {}
for _ in range(n):
    address, pw = input().split()
    dict[address] = pw
for _ in range(m):
    test = input().rstrip()
    print(dict[test])