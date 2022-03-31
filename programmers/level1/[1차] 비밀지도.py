# 더 쉬운 풀이
def solution(n, arr1, arr2):
    answer = []
    for num1, num2 in zip(arr1, arr2):
        result = bin(num1|num2)[2:] # bitwise 연산자
        result = "0" * (n-len(result)) + result
        result = result.replace("1", "#")
        result = result.replace("0", " ")
        answer.append(result)
    return answer

# =======================================

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