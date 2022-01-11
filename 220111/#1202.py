n, k = map(int, input().split())

jewelry_list = []
bag_list = []
total = 0

for _ in range(n):
    weight, cost = map(int, input().split())
    jewelry_list.append((weight, cost))

jewelry_list.sort(reverse=True, key=lambda x:(x[1], x[0]))

bag_list = [int(input()) for _ in range(k)]

for i in range(k):
    idx = 0
    while idx < n:
        if bag_list[i] >= jewelry_list[idx][0]:
            total += jewelry_list[idx][1]
            jewelry_list.pop(idx)
            n -= 1
            break
        idx += 1

print(total)
