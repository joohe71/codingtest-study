# 참고 : https://velog.io/@munang/%EA%B0%9C%EB%85%90%EC%A0%95%EB%A6%AC-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%8B%A4%EC%A4%91-%EC%A7%91%ED%95%A9
# 참고 : https://velog.io/@munang/%EA%B0%9C%EB%85%90%EC%A0%95%EB%A6%AC-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B0%9D%EC%B2%B4%EC%A7%80%ED%96%A5-%EC%83%81%EC%9A%A9%EA%B5%AC

import math

def make_list(str1,arr1,a):
    for i in range(len(str1)-1):
        arr1.append(str1[i:i+2])
        
    for i in arr1:
        if i.isalpha():
            a.append(i)
    return a


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    arr1 = []
    arr2 = []
    a = []
    b= []
    make_list(str1,arr1,a)
    make_list(str2,arr2,b)

    a_temp = a.copy()
    a_result = a.copy()
    intersection = []
    
    for i in b:
        if i not in a_temp:
            a_result.append(i) # a U b
        else:
            a_temp.remove(i) # a에서 교집합 제거 => a - (a 교 b) => 순수 a
            intersection.append(i)
    
    
    if not a_result and not intersection:
        answer = 65536
    else:
        answer = math.floor(len(intersection)/len(a_result)*65536)
    
    return answer