# 입력
num = list(map(int,input().split()))

# 출력
# sort와 sorted의 차이점
# sort : 리스트를 제자리에서 수정 -> 원래 변수가 수정됨.
# sorted : 반환값이 배열값: 변수에 저장 가능! 원래 변수는 수정되지 않음
ascending = sorted(num)
descending = sorted(num, reverse=True)
if num == ascending:
    print("ascending")
elif num == descending:
    print("descending")
else:
    print("mixed")