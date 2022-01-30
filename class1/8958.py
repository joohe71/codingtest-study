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