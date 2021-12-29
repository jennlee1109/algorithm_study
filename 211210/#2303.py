n = int(input())

max_total = 0
answer = 0

for id in range(n):
    num = list(map(int, input().split()))

    for i in range(len(num)):
        for j in range(i+1, len(num)):
            for k in range(j+1, len(num)):
                total = (num[i] + num[j] + num[k]) % 10
                # print(num[i], num[j], num[k], total, id+1)
                if max_total <= total:
                    answer = id + 1
                    max_total = total

print(answer)
