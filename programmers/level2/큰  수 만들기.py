## 시간 초과

# from itertools import combinations

# def solution(number, k):
#     answer = 0
#     for i in combinations(list(number), len(number)-k):
#         if answer < int(''.join(i)):
#             answer = int(''.join(i))
    
#     return str(answer)

def solution(number, k):
    # stack에 입력값을 순서대로 삽입 
    stack = [number[0]]
    for num in number[1:]:
        # 들어오는 값이 stack 값보다 크면, 기존의 값을 제거하고 새로운 값으로 바꿈 
        while stack and stack[-1] < num and k > 0:
            # 값을 한개 빼서 k는 1이 제거 
            k -= 1
            # 내부의 값을 제거 
            stack.pop()
            # print("pop : ",stack)
        
        # 새로운 값을 삽입 
        stack.append(num)
        
        # print(stack)
        
    # 만일 충분히 제거하지 못했으면 남은 부분은 단순하게 삭제
    # 이렇게 해도 되는 이유는 이미 큰 수부터 앞에서 채워넣었기 때문 
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)
