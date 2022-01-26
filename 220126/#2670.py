n = int(input())
num_list = [float(input()) for _ in range(n)]

result = num_list[0]
for i in range(n):
    for j in range(i, n):
        if num_list[i] <= num_list[j]:
            total = num_list[i]
            for k in range(i+1, j+1):
                total *= num_list[k]
            # print(num_list[i:j+1], result, total)
            if result <= total:
                result = total

print(round(result, 4))