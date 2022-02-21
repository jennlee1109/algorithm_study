import sys

path = sys.stdin.readline()

N = len(path)
x = []
y = []

for i in range(N - 1):
    if path[i] == '(' and path[i + 1] == '(':
        x.append((i, i + 1))
    elif path[i] == ')' and path[i + 1] == ')':
        y.append((i, i + 1))

result = 0
for i in range(len(x)):
    for j in range(len(y)):
        if x[i][0] < y[j][0] and x[i][1] < y[j][1]:
            result += 1

print(result)
