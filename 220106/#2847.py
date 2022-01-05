n = int(input())

levels = list(int(input()) for _ in range(n))

cnt = 0

for idx in range(n-1, 0, -1):
    if levels[idx] <= levels[idx-1]:
        gap = levels[idx-1] - levels[idx] + 1
        cnt += gap
        levels[idx-1] -= gap

print(cnt)