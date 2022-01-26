n = int(input())
num_list = [float(input()) for _ in range(n)]

dp = [num_list[0]]

for i in range(1, n):
    dp.append(max(num_list[i], dp[i-1] * num_list[i]))

print("{0:.3f}".format(max(dp)))