n = int(input())

weights = [int(input()) for _ in range(n)]
weights.sort()

result = weights[0] * n

while True:
    if n == 1:
        break

    weights.pop(0)
    n -= 1
    if result > weights[0] * n:
        break

    result = weights[0] * n

print(result)
