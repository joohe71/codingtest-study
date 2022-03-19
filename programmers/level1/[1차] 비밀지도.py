def code(n, arr, bucket): # (n, 배열, 암호화된 값 담아줄 배열)
    for i in arr:
        x = format(i, 'b')
        if len(x) < n:
            x = '0' * (n-len(x)) + x
        bucket.append(list(x))
    for i in bucket:
        for j in range(n):
            if i[j] == "0":
                i[j] = " "
            else:
                i[j] = "#"
    # print(bucket)
    return bucket
    

def solution(n, arr1, arr2):
    one = []
    two = []
    code(n, arr1, one)
    code(n, arr2, two)
    for i in range(len(one)):
        for j in range(n):
            if one[i][j] == " ":
                one[i][j] = two[i][j]
    answer = []
    for i in one:
        answer.append("".join(i))
    return answer