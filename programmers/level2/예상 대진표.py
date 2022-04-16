def repeat(n_list,a,b):
    arr = [(n_list[2*i],n_list[2*i+1]) for i in range(len(n_list)//2)]
    new_arr = []
    for values in arr:
        if a in values and b in values:
            new_arr = []
            break
        elif a in values:
            new_arr.append(a)
        elif b in values:
            new_arr.append(b)
        else:
            new_arr.append(values[0])
    
    return new_arr


def solution(n,a,b):
    n_list = [i for i in range(1,n+1)]
    cnt = 1
    while len(n_list) > 2:
        n_list = repeat(n_list,a,b)
        if not n_list:
            break
        
        cnt += 1
        # print(n_list, cnt)

    return cnt