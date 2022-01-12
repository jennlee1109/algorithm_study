import sys
n, k = map(int, input().split())

num = sys.stdin.readline()
num_list = [int(num[i]) for i in range(n)]

result = ''
cnt = 0
i = 0

while i < len(num_list)-1:
    if cnt == k:
        break
    if num_list[i] < num_list[i+1]:
        num_list.pop(i)
        cnt += 1
        i = 0
    else:
        i += 1


for i in range(len(num_list)):
    print(num_list[i],end="")