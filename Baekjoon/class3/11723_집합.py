# 정답 처리 1
# import sys
# input = sys.stdin.readline

# num = int(input()) # 수행해야 하는 연산의 수

# s = [] #비어있는 공집합

# for _ in range(num):
#     calc = list(input().split()) # ["add", "3"]
#     operation = calc[0]
#     # value = calc[1]
#     if operation == "add":
#         if value not in s:
#             s.append(value)
#     elif operation == "remove":
#         if value in s:
#             s.remove(value)
#     elif operation == "check":
#         if value in s:
#             print(1)
#         else:
#             print(0)
#     elif operation == "toggle":
#         if value in s:
#             s.remove(value)
#         else:
#             s.append(value)
#     elif operation == "all":
#         s = [j for j in range(1,21)] # 리스트에 str값으로 변환해서 받으면 시간이 더 오래걸림! 
#     elif operation == "empty":
#         s = []
#     print(s)
# ========================================================================================

# 정답 처리 2
# set 자료형 사용하기 => 중복 허용하지 않는다, 순서가 없다(unordered)
# 교집합( '&' 연산자 또는 intersection 사용)
# 합집합( '|' 연산자 또는 union 사용)
# remove는 존재하지 않는 대상을 지우면 error 발생 / discard는 존재하지 않음을 보장 not error

import sys
input = sys.stdin.readline

num = int(input()) # 수행해야 하는 연산의 수

s = set() #비어있는 공집합

for _ in range(num):
    calc = list(input().split()) # ["add", "3"]
    operation = calc[0]
    if len(calc) == 1:
        if operation == "all":
            s = set([j for j in range(1,21)])
        elif operation == "empty":
            s = set()
    else:
        value = int(calc[1])
        if operation == "add":
            if value not in s:
                s.add(value)
        elif operation == "remove":
            if value in s:
                s.discard(value)
        elif operation == "check":
            if value in s:
                print(1)
            else:
                print(0)
        elif operation == "toggle":
            if value in s:
                s.discard(value)
            else:
                s.add(value)

