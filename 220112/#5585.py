money = int(input())

money = 1000 - money

coins = [500, 100, 50, 10, 5, 1]
total = 0

for i in range(len(coins)):
    if money >= coins[i]:
        total += money // coins[i]
        money = money - (money // coins[i]) * coins[i]

    if money <= 0:
        break

print(total)