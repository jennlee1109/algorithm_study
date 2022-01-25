n, m = map(int, input().split())

direction = [(-2, 1), (-1, 2), (1, 2), (2, 1)]

map = [[0 for _ in range(m)] for _ in range(n)]

for m1 in map:
    print(m1)

queue = [(0, 0)]
cnt = 1
map[0][0] = 1

while queue:
    x, y = queue.pop(0)
    # print('x', x, 'y', y, end=" ")

    for i in range(4):
        xx = x + direction[i][0]
        yy = y + direction[i][1]
        # print(direction[i][0], direction[i][1])
        if 0 <= xx < n and 0 <= yy < m:
            if map[xx][yy] == 0:
                # print(xx, yy)
                cnt += 1
                map[xx][yy] = cnt
                queue.append((xx, yy))
                break

print(cnt)
for m1 in map:
    print(m1)
