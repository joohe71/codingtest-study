# # 스택(stack)은 제한적으로 접근할 수 있는 나열 구조이다. 그 접근 방법은 언제나 목록의 끝에서만 일어난다.
# # 스택은 한 쪽 끝에서만 자료를 넣거나 뺄 수 있는 선형 구조(LIFO - Last In First Out)으로 (즉, 후입선출법, 항아리구조) 되어 있다. 자료를 
# # 넣는 것을 '밀어넣는다' 하여 푸쉬(push)라고 하고 반대로 넣어둔 자료를 꺼내는 것을 팝(pop)이라고 하는데, 이때 꺼내지는 자료는 가장 최근에 
# # # 푸쉬한 자료부터 나오게 된다.


import sys
input = sys.stdin.readline
while(1):
    sentence = input().rstrip() #개행 삭제
    if (sentence == "."):
        break
    
    arr = []
    for i in sentence:
        if i =="(" or i == "[": #열린 괄호가 나오면 append
            arr.append(i)
        elif i == ")":
            if arr and arr[-1] == "(": 
                arr.pop()
            else:
                arr.append(i)
            
        elif i == "]":
            if arr and arr[-1] == "[":
                arr.pop()
            else:
                arr.append(i)


    if len(arr) == 0: #짝이 맞는다면 빈 배열이므로
        print("yes")
    else:
        print("no")


