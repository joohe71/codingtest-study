t = int(input())
for i in range(t):
    h,w,n = map(int,input().split()) #호텔의 층 수(높이), 각 층의 방 수(가로), 몇번째 손님
    if h >= n:
        print(100*n + 1)
    else:
        q = n // h # 몫
        r = n % h # 나머지
        if r == 0:
            print(h*100 + q)
        else:
            print(r*100 + q + 1 )

# # 다른 풀이
# n = int(input())
# for _ in range(n):
#   h, w, n = map(int, input().split())
#   if n%h==0:
#     print(int(h*100+n/h))
#   elif h>n:
#     print(int(n*100+1))
#   else:
#     print(int(n%h*100+n/h+1))