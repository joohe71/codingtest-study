# # 첫번쨰 시간초과
# import sys
# input = sys.stdin.readline
# n, m = map(int,input().split())
# dict_example = {}
# for i in range (1,n+1):
#     example = input().rstrip() # 개행삭제
#     dict_example[example] = i
# # print(dict_example.items())
# for _ in range(m):
#     test = input().rstrip()
#     for key, value in dict_example.items(): # dict_example.items() => (key,value)쌍으로 리스트로 변환
#         if test == key:
#             print(value)
#         elif test == str(value):
#             print(key)


# # 두번째 시간초과
# import sys
# input = sys.stdin.readline
# n, m = map(int,input().split())
# dict_example = {}
# for i in range (1,n+1):
#     example = input().rstrip() # 개행삭제
#     dict_example[example] = i
# # print(dict_example.items())
# for _ in range(m):
#     test = input().rstrip()
#     if test.isdigit():
#         print(list(dict_example.keys())[int(test)-1])
#     else:
#         print(dict_example[test])


## 정답처리
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
dict_example = {}
for i in range (1,n+1):
    example = input().rstrip() # 개행삭제
    dict_example[example] = i # 포켓몬 이름: 번호
    dict_example[i] = example # 번호: 포켓몬 이름
# print(dict_example.items())
for _ in range(m):
    test = input().rstrip()
    if test.isdigit():
        print(dict_example[int(test)])
    else:
        print(dict_example[test])