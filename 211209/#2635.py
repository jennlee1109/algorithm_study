num = int(input())

max_val = 0
answer = []

for i in range(num, -1, -1):
    result = [num, i]

    tmp = num - i
    i, j = 0, 1
    while tmp >= 0:
        result.append(tmp)
        i += 1
        j += 1
        tmp = result[i] - result[j]

    if max_val <= len(result):
        answer = result
        max_val = len(result)

print(max_val)
for idx in range(max_val):
    print(answer[idx], end=" ")