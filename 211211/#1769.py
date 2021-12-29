x = input()

cnt = 0

if len(x) > 1:
    total = 11

    while total >= 10:
        cnt += 1
        total = 0

        for i in range(len(x)):
            total += int(x[i])
        x = str(total)

else:
    total = int(x)

print(cnt)

if total % 3 == 0:
    print('YES')
else:
    print('NO')
