def solution(s):
    arr = list(s.split(" "))
    for i in range(len(arr)):
        if len(arr[i]) == 1:
            arr[i] = arr[i].upper()
        elif len(arr[i])>=2:
            arr[i] = arr[i][0].upper() + arr[i][1:].lower()
    
    return " ".join(arr)