# 처음에 시간초과 난 이유 => 첫번째 반복문에서 arr 사용
# 해결 방법 => 중복 제거된 set_arr 사용

def solution(s):
    s = s.replace("{","").replace("}","")
    arr = list(s.split(","))
    set_arr = set(arr)
    dict = {}
    for i in set_arr:
        dict[i] = arr.count(i)
        
    answer = []
    for key, value in sorted(dict.items(),key=lambda x:x[1], reverse=True):
        answer.append(int(key))
    
    return answer