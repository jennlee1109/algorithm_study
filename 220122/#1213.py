word = input()

cnt = 0
word_dic = dict()

left = ''
result = ''

for i in range(len(word)):
    if word[i] in word_dic:
        word_dic[word[i]] += 1
    else:
        word_dic[word[i]] = 1

sorted_list = sorted(word_dic.items(), key=lambda x:x[0])

for key, val in sorted_list:
    if val % 2 == 1:
        cnt += 1
        result += key
    left += key * (val // 2)

if cnt > 1:
    print("I'm Sorry Hansoo")
else:
    print(left + result + left[::-1])