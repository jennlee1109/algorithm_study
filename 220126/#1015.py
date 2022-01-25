n = int(input())

a = list(map(int, input().split()))
sorted_a = sorted(a)

for i in range(n):
    for j in range(n):
        if sorted_a[j] == a[i]:
            print(j, end=" ")
            sorted_a[j] = -1
            break