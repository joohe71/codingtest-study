# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 딕셔너리에서는 키의 값이 중복되지 않는다는 점 이용

n = int(input())
dict = {}
for _ in range(n):
    words = input()
    dict[words] = len(words) # key와 value 값

# 딕셔너리는 sorted()함수를 이용하여 정렬가능
# d.items() 를 하여 각 key, value 가 tuple로 들어있는 
# 리스트 (dict_items 객체) 로 만듭니다
# sorted는 tuple pair로 이루어진 list를 return
# 비교할 요소가 복수 개일 경우, 튜플로 우선순위를 정해줄 수 있다.
# -를 붙이면 현재와 반대차순으로 정렬된다.
# 길이, 사전 순으로 정렬
a = sorted(dict.items(),key=lambda x: (x[1],x[0])) 
for i in range(len(a)):
    print(a[i][0])


# for i in range(len(words_list)):
#     print(words_list[i])

    
