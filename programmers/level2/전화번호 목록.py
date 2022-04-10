# 문자형 숫자는 sort 사용 시 => 순서로 인식하여 정렬한다.
# https://didalsgur.tistory.com/entry/Python-%EB%AC%B8%EC%9E%90%ED%98%95-Character-%EC%88%AB%EC%9E%90-%EC%A0%95%EB%A0%AC-sort-key

def solution(phone_book):
    answer = True
    phone_book.sort(key = lambda x: (x,len(x)))
    # print(phone_book)
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer= False
            break
    return answer