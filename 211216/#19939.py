n, k = map(int, input().split())

least_sum = (k * (k+1)) // 2

if least_sum > n:
    print(-1)

else:
    if (n - least_sum) % k == 0:
        print(k-1)
    else:
        print(k)
