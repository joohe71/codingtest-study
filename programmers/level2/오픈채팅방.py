def solution(record):
    dict = {}
    answer = []
    for i in record:
        if i.startswith("Change"):
            word, user_id, name = i.split(' ')
            dict[user_id] = name

        if i.startswith("Enter"):
            word, user_id, name = i.split(' ')
            dict[user_id] = name
    
    
    for i in record:
        if i.startswith("Enter"):
            word, user_id, name = i.split(' ')
            answer.append(dict[user_id]+"님이 들어왔습니다.")
            
        if i.startswith("Leave"):
            word, user_id = i.split(' ')
            answer.append(dict[user_id]+"님이 나갔습니다.")
    
    return answer