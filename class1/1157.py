alphabet = list(input().upper())
alphabet_0 = list(set(alphabet)) #중복제거

count_list = []
for i in alphabet_0:
    count = alphabet.count(i)
    count_list.append(count)

if count_list.count(max(count_list)) >= 2:
    print("?")
else:
    print(alphabet_0[count_list.index(max(count_list))])
