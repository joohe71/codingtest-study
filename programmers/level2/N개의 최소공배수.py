def lcm(a,b):
    for i in range (max(a,b), (a*b)+1):
        if i % a == 0 and i % b == 0:
            return i
            break

def solution(arr):
    for i in range(len(arr)-1):
        minimum = lcm(arr[i],arr[i+1])
        arr[i+1] = minimum
    return arr[-1]