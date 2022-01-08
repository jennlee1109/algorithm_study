import sys
n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()

m = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    start = 0
    end = n-1
    flag = False

    while start <= end:
        mid = (start + end) // 2

        if num_list[mid] == target[i]:
            print(1, end=" ")
            flag = True
            break

        if num_list[mid] < target[i]:
            start = mid + 1
        else:
            end = mid - 1

    if not flag:
        print(0, end=" ")