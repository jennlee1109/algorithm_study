import sys

n, m = map(int, sys.stdin.readline().split())

# worst = [[] for _ in range(n+1)]
num_set = [0] * (n+1)
answer = 0
cnt = 0
worst_combination = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    num_set[a] += 1
    num_set[b] += 1

    worst_combination += n - 2

for i in range(1, n+1):
    if num_set[i] >= 2:
        cnt += 1

print((n * (n-1) * (n-2)) // 6 - (worst_combination - cnt))
