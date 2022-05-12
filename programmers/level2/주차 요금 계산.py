import math
def Minutes(date):
    h, m = map(int, date.split(':'))
    return h*60 + m

def solution(fees, records):
    dict = {}
    for i in records:
        t, num, h = i.split(" ")
        num = int(num)
        if h == "IN":
            if num in dict:
                dict[num].append([h,t])
            else:
                dict[num] = [[h,t]]
            
        else:
            dict[num].append([h,t])
    # print(dict)
    arr = sorted(dict.items(),key=lambda x : x[0])
    # print(arr)
    for i in arr:
        if len(i[1])%2 == 1:
            i[1].append(["OUT","23:59"])
    answer = {}
    for i in arr:
        for j in range(1,len(i[1])//2+1):
            cal = -Minutes(i[1][2*(j-1)][1])+Minutes(i[1][2*j-1][1])
            if i[0] not in answer:
                answer[i[0]] = cal
            else:
                answer[i[0]] = answer[i[0]] + cal
            
    for i in answer:
        if answer[i] - fees[0] < 0:
            answer[i] = fees[1]
        else:
            answer[i] = fees[1] + math.ceil((answer[i]-fees[0])/fees[2]) * fees[3]
    return list(answer.values())