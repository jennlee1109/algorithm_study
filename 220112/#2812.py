import sys
n, k = map(int, input().split())

num = sys.stdin.readline()
num_list = [int(num[i]) for i in range(n)]
stack = []
cnt = 0

for i in range(n):
    while cnt < k and stack and stack[-1] < num_list[i]:
        stack.pop()
        cnt += 1
    stack.append(num_list[i])

for s in stack[:n-k]:
    print(s,end="")