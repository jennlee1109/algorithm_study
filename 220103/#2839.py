sugar = int(input())

total = 0

n = sugar

while n > 0:
    if n >= 5:
        total += n // 5
        n -= 5 * (n//5)
        while n % 3 != 0 and sugar > n:
            n += 5
            total -= 1

    if n % 3 == 0:
        total += n // 3
        n -= 3 * (n//3)
    else:
        total = -1
        break

print(total)