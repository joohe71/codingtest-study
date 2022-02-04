# 숫자말고 문자열로 하면 더 쉬움
# 아래는 숫자의 경우

while (1==1):
    num = int(input())
    reversed_num = list(map(int,str(num)))
    reversed_num.reverse()
    reversed_num = ''.join(map(str,reversed_num)) #join은 문자열을 합한다(not 숫자)
    if num == 0:
        break
    else:
        if (num == int(reversed_num)):
            print("yes")
        else:
            print("no")

# # 다른 풀이(직접 인덱스로 접근하는 방법)
# while(1==1):
#     flag = 1
#     n = input()
#     if n == "0":
#         break

#     for i in range(len(n)):
#         if n[i] != n[len(n)-1-i]:
#             print("no")
#             flag = 0
#             break
#     if flag == 1:
#         print("yes")
