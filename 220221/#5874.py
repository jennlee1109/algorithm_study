import sys

path = sys.stdin.readline()

result = 0
cnt = 0

for i in range(len(path)-1):
    if path[i] == path[i+1]:
        if path[i] == '(':
            cnt += 1
        else:
            result += cnt

print(result)