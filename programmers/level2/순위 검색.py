# 이분 탐색 이용해야 하는 문제






# 효율성 테스트 미통과
def solution(info, query):
    dict = {}
    answer = []
    for i, j in enumerate(query):
        query[i] = j.replace(" and ", " ")
    # print(query)
    
    for index, data in enumerate(info):
        dict[index] = list(data.split(" "))
    
    for i in query:
        wanted = list(i.split(" "))
        
        arr = [i for i in dict.values() if int(i[-1])>=int(wanted[-1])]
        # print(arr)
        cnt = 0
        for i in arr:
            passed = 0
            for j in range(4):
                if i[j] == wanted[j] or wanted[j] == "-":
                    passed += 1
            if passed == 4:
                cnt += 1
        answer.append(cnt)
    return answer