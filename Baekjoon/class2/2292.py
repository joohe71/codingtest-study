# n = int(input())

# num_pileup = 1 #벌집의 개수, 1개부터 시작
# cnt = 1
# while (n > num_pileup):
#     num_pileup += 6*cnt
#     cnt += 1
# print(cnt)

#등차수열의 합공식
n = int(input())
last = 1
road = 1
if (n == 1):
    print(road)
else:
    for i in range(1,100000):
        last += 6 * i
        road += 1
        if (n <= last):
            print(road)
            break