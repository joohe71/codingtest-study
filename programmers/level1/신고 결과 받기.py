def solution(id_list, report, k):
    users = {} # key에게 신고한 사람들
    ban_users = {} # 신고당한 횟수
    answer = {}
    for i in id_list:
        answer[i] = 0

    for i in id_list:
        ban_users[i]=0

    for i in id_list:
        users[i] = []
    for i in set(report):
        user, ban_user = i.split(' ')
        users[ban_user].append(user)
        ban_users[ban_user]+=1
    
    for key,values in users.items():
        if ban_users[key]>=k:
            for v in values:
                answer[v]+=1




    return list(answer.values())
    
## 시간 초과

# def solution(id_list, report, k): 
#     dict_report = {}
#     dict_id_list = {}
#     answer = []
#     for i in id_list:
#         dict_id_list[i] = [0,0] #[신고당한 횟수, 처리결과 메일 받은 횟수]
    
#     for i in range(len(report)):
#         dict_report[i] = list(report[i].split())

#     arr_report = list(dict_report.values())
#     arr_report_real = []
#     for i in arr_report:
#         if i not in arr_report_real:
#             arr_report_real.append(i)
                
#     for i in id_list:
#         for j in arr_report_real:
#             if i == j[1]:
#                 dict_id_list[i][0] += 1


#     for key in dict_id_list:
#         for j in arr_report_real:
#             if (dict_id_list[key][0] >= k) and (j[1] == key):
#                 dict_id_list[j[0]][1] += 1

#     for i in list(dict_id_list.values()):
#         answer.append(i[1])

#     return answer

    
print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],2))
