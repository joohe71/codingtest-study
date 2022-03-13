n = int(input())
dict = {}
for i in range(n):
    x, y = map(int,input().split())
    dict["loc"+ str(i+1)] = [x, y]

li = sorted(dict.items(),key =lambda a:(a[1][0],a[1][1]))
for j in range(len(li)):
    print(li[j][1][0],li[j][1][1], sep=" ")

# # 좀 쉬운 방법 (tuple 이용)
# import sys
# n = int(sys.stdin.readline())
# arr = []
# for _ in range(n):
#     arr.append(tuple(map(int,sys.stdin.readline().split())))

# arr.sort(key = lambda x: (x[0],x[1]))
# for i in range(len(arr)):
#     print(arr[i][0],arr[i][1], sep=" ")
