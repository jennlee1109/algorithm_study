word = input().split()
ucpc = 'UCPC'
result = ''
for i in range(len(word)):
    for j in range(len(word[i])):
        if word[i][j].isupper():
            result += word[i][j]

idx = 0

for r in result:
    if r == ucpc[idx]:
        idx += 1

        if idx == len(ucpc):
            break

# print(result, idx)

if idx == 4:
    print('I love UCPC')
else:
    print('I hate UCPC')