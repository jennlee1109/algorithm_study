a, p = map(int, input().split())

num_list = []

target = a
cnt = 0

while target not in num_list:
    num_list.append(target)
    tmp = str(target)

    next_target = 0
    for i in range(len(tmp)):
        next_target += int(tmp[i]) ** p
    target = next_target

num_list.append(target)

for i in range(len(num_list)):
    if num_list[i] != num_list[-1]:
        cnt += 1
    else:
        print(cnt)
        break