import sys

n = int(sys.stdin.readline())

paper = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

total = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(101):
    for j in range(101):
        if paper[i][j] == 1:
            cnt = 0
            for k in range(4):
                r, c = i + dx[k], j + dy[k]
                if 0 <= r < 101 and 0 <= c < 101:
                    if paper[r][c] == 0:
                        cnt += 1

            if cnt == 2:
                total += 2
            elif cnt == 1:
                total += 1

print(total)
