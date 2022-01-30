target = int(input())

cnt = 1

start = 1
end = start + 1

total = start

while end < target - 1 and start <= target // 2:
    if total == target:
        cnt += 1
        total -= start
        total += end
        end += 1
        start += 1
    else:
        if total < target:
            total += end
            end += 1
        else:
            total -= start
            start += 1

print(cnt)
