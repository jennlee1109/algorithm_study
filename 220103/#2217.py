n = int(input())

weights = [int(input()) for _ in range(n)]
weights.sort()

result = []

for i in range(n):
    result.append(weights[i] * n)
    n -= 1

print(max(result))