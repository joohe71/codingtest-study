from itertools import permutations

# isdigit() => 음수는 false로 인식한다.
def stacking(string, j):
    stack = []
    stack.append(string[0])
    while len(stack)<2:
        for k in range(1,len(string)):
            last = stack[-1]
            if not last.lstrip("-").isdigit() and last == j:
                if j == '+':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(str(int(b) + int(string[k])))
                elif j == '-':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(str(int(b) - int(string[k])))
                elif j == '*':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(str(int(b) * int(string[k])))
            else:
                stack.append(string[k])
    return stack
    
    
def operation(string):
    op = string[1]
    num = int(string[0])
    for j in range(2,len(string)):
        if string[j].lstrip("-").isdigit():
            if op == "*":
                num *= int(string[j])
            elif op == "+":
                num += int(string[j])
            elif op == "-":
                num -= int(string[j])
    return num    


def solution(expression):
    string = expression.replace("+"," + ").replace("-"," - ").replace("*"," * ")
    string = list(string.split(" "))
    sign = []
    
    for i in string:
        if i.isdigit():
            pass
        else:
            if i not in sign:
                sign.append(i)
            
    arr = list(permutations(sign,len(sign)))
    
    max_num = 0
    for i in arr:
        if len(i) == 1:
            num = operation(string)
        
        elif len(i) == 2: 
            a = stacking(string,i[0])
            num = operation(a)
            
        elif len(i) == 3: 
            a = stacking(string,i[0])
            b = stacking(a,i[1])
            num = operation(b)

            
        max_num = max(max_num, abs(num))
            
    return max_num