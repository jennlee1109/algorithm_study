import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

total = 0
tmp = 0

for i in range(n-1, 0, -1):
    tmp += num_list[i]
    total += num_list[i-1] * tmp

print(total)