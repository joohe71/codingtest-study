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

# # 다른 풀이 1
# word = input().upper()
# result = {}

# for i in word:
#   if i not in result:
#     result[i] = 1
#   else:
#     result[i] +=1

# reverse_result = dict(map(reversed,result.items()))

# if list(result.values()).count(max(result.values())) >=2:
#   print("?")
# else:
#   print(reverse_result[max(result.values())])


# # 다른 풀이 2
# a = input().upper()
# dic = {}
# count = 0

# for i in a:
#   if i not in dic:
#     dic[i] = 1
#   else:
#     dic[i] += 1

# for x,y in dic.items():
#   if y == max(dic.values()):
#     count+=1

# sorted_dic = sorted(dic.items(), key=lambda x: -x[1])

# if count > 1:
#   print("?")
# else:
#   print(sorted_dic[0][0])