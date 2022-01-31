n, k = map(int, input().split())

bucket_list = dict()
min_position = 1000000
max_position = 0
for i in range(n):
    weight, position = map(int, input().split())
    bucket_list[position] = weight
    max_position = max(max_position, position)
    min_position = min(min_position, position)

result = 0
end = min_position
total = 0

for start in range(min_position, max_position + 1):
    while end < max_position + 1 and end - start <= k * 2:
        if end in bucket_list:
            total += bucket_list[end]

        end += 1

    result = max(result, total)
    if start in bucket_list:
        total -= bucket_list[start]

print(result)
