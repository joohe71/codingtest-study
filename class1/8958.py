num = int(input())
for i in range(num):
    test = list(input())
    score = []
    for j in range(len(test)):
        if test[j] == "O":
            if j == 0 or test[j-1] != test[j]:
                score.append(1)
            else:
                score.append(score[j-1]+1)
        else:
            score.append(0)
    print(sum(score))


# # 다른 코드
# n = int(input())
# for _ in range(n):
#     p = input()
#     score = 0
#     n_sum = 0
#     for i in p:
#         if p == "O":
#             score += 1
#             n_sum += score
#         else:
#             score = 0
#     print(n_sum)