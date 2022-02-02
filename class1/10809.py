# 아스키 코드에서 영어 소문자는 97~122
s = input()
alphabet = list(range(97,123)) #chr은 아스키코드를 문자열로 변환
for i in alphabet:
    print(s.find(chr(i)),end=" ")


