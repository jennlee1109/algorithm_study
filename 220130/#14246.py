n = int(input())
num_list = list(map(int, input().split()))
k = int(input())

cnt = 0
j = 0
total = 0

for i in range(n):
    while j < n and total <= k:
        total += num_list[j]
        j += 1

    if total > k:
        cnt += n - j + 1

    total -= num_list[i]


print(cnt)