import sys

n = int(sys.stdin.readline())

paper = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(10):
        for j in range(10):
            paper[x + i][y + j] = 1

total = 0
for i in range(101):
    total += sum(paper[i])

print(total)
