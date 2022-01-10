n = int(input())

cards = [int(input()) for _ in range(n)]

cards.sort()
result = []
total = 0
tmp = cards[0]

for i in range(1, n):
    tmp += cards[i]
    total += tmp

result.append(total)

idx = 0
tmp = 0
total = 0

for i in range(n):
    if i % 2 == 0 or i == n-1:
        if i == n-1:
            tmp += cards[i]
        total += tmp * (n // 2)
        tmp = cards[i]
    else:
        tmp += cards[i]


result.append(total)
print(result)

print(min(result))
