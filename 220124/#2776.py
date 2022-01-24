import sys

for _ in range(int(input())):

    n = int(sys.stdin.readline())
    note1 = list(map(int, sys.stdin.readline().split()))
    note1.sort()

    m = int(sys.stdin.readline())
    note2 = list(map(int, sys.stdin.readline().split()))

    for idx in range(m):
        low, high = 0, n-1
        result = 0

        while low <= high:
            mid = (low + high) // 2

            if note2[idx] == note1[mid]:
                result = 1
                break

            if note2[idx] < note1[mid]:
                high = mid - 1
            else:
                low = mid + 1

        print(result)