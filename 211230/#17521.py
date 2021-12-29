n, w = map(int, input().split())

coin_prices = []

max_coin = 1
min_coin = 100000
coin = 0
cash = w

for _ in range(n):
    price = int(input())
    coin_prices.append(price)

for day in range(n-1):
    if coin_prices[day] < coin_prices[day+1]:
        coin += cash // coin_prices[day]
        cash = cash % coin_prices[day]

    elif coin_prices[day] > coin_prices[day-1]:
        cash += coin * coin_prices[day]
        coin = 0

if coin > 0:
    cash += coin * coin_prices[-1]

print(cash)