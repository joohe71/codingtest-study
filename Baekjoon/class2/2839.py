# 1) 5kg 에 설탕을 빠짐없이 담을 수 있다면 (입력 값이 5로 나눠떨어진다면) 입력값을 5로 나눈 몫을 출력하고 프로그램 종료
# 2) 5kg 에 설탕을 빠짐없이 담을 수 없다면 3kg 봉지에 한 번 담기 (봉지 카운트는 1 증가, 입력값은 3 감소)
# 3) 만약 입력값이 0보다 작아지면 -1을 출력하고 프로그램 종료
n = int(input())
r = n % 5 #나머지
q = n // 5 #몫
if r == 0 :
    print(q)
else:
    while (1==1):
        if r % 3 == 0:
            if q < 0:
                print(-1)
            else:
                print(q + r//3)
            break
        else:
            r += 5
            q -= 1
