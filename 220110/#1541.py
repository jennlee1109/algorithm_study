expression = input().split('-')

total = 0

for i in range(len(expression)):
    if not expression[i].isdigit():
        num_list = expression[i].split('+')
        tmp = 0
        for num in num_list:
            tmp += int(num)
        if i == 0:
            total += tmp
        else:
            total -= tmp

    else:
        if i == 0:
            total = int(expression[0])
        else:
            total -= int(expression[i])

print(total)