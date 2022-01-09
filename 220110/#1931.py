n = int(input())

times = []

for _ in range(n):
    start, end = map(int, input().split())
    times.append((start, end))

times.sort(key=lambda x: (x[1], x[0]))

prev_end = 0
cnt = 0

for start, end in times:
    if start >= prev_end:
        prev_end = end
        cnt += 1
        # print(start, end, '--', prev_end)

print(cnt)
