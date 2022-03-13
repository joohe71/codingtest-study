l = int(input())
str = list(input())
alphabet = list('abcdefghijklmnopqrstuvwxyz')
my_list = []
for i in range(len(alphabet)):
    for j in range(len(str)):
        if alphabet[i] == str[j]:
            value = (i+1) * 31**j
            my_list.append(value)

print(sum(my_list)%1234567891)