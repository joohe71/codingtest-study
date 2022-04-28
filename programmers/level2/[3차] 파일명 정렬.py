def solution(files):
    answer = []
    for a in files:
        head = '' 
        number = ''
        tail = ''

        check = False
        for i in range(len(a)): 
            if a[i].isdigit():  
                number += a[i]
                check = True
            elif not check:  
                head += a[i]
            else:               
                tail = a[i:]
                break
        answer.append((head, number, tail))  

    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))  

    return [''.join(t) for t in answer]