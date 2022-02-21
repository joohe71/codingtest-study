# 괄호를 쳐서 최소값 만들기
# +연산자를 최대한 -로 변경해주는 것이 필요
## 테스트 케이스 => 1+2-3+5-3+5

import sys
input = sys.stdin.readline
num = input().rstrip() #개행 삭제

numminus = num.split('-') # 마이너스 연산자로 쪼갠 리스트
numplus = num.split('+') # 플러스 연산자로 쪼갠 리스트

result1 = 0

if (''.join(numplus).isdigit()): # 플러스로만 이루어졌을 경우
    result = sum(list(map(int,numplus)))
else: # 그 외의 경우
    numminus_1st = numminus.pop(0) # 첫번 쨰 값이 양수인지 음수인지 확인하기 위해

    for i in numminus:
        a = list(map(int,i.split('+')))
        result1 += -sum(a)
    
    if (numminus_1st == ""): # 처음 값이 음수이면
        result = result1
    else:
        numminus_1st = list(map(int,''.join(numminus_1st).split('+'))) #처음 값이 양수이면
        result = sum(numminus_1st) + result1
        
print(result)