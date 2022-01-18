import math

n, m = map(int, input().split())

set = []
piece = []

for i in range(m):
    s, p = map(int, input().split())
    set.append(s)
    piece.append(p)

set_count = math.ceil(n / 6)

min_val = float("inf")

for k in range(set_count + 1):
    for i in range(m):
        total = 0
        if k == 0:
            total = set[i] * (set_count - k)
            min_val = min(total, min_val)
        else:
            for j in range(m):
                total = set[i] * (set_count - k) + piece[j] * (n - 6 * (set_count - k))
                min_val = min(total, min_val)

print(min_val)
