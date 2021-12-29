n, w = map(int, input().split())

coin_prices = []

max_coin = 1
min_coin = 100000
coin = 0
cash = w

for _ in range(n):
    price = int(input())
    coin_prices.append(price)
    if max_coin < price:
        max_coin = price
    if min_coin > price:
        min_coin = price

# print(coin_prices, max_coin, min_coin)

for day in range(n):
    if day == 0:
        if coin_prices[day] <= coin_prices[day+1] and coin_prices[day] < max_coin:
            coin += cash // coin_prices[day]
            cash -= coin * coin_prices[day]

    elif day == n-1:
        if coin_prices[day] >= coin_prices[day-1] and coin_prices[day] > min_coin:
            cash += coin_prices[day] * coin
            coin = 0

    else:
        if coin_prices[day-1] < coin_prices[day] and coin_prices[day] > coin_prices[day+1]:
            cash += coin_prices[day] * coin
            coin = 0
        elif coin_prices[day-1] > coin_prices[day] and coin_prices[day] < coin_prices[day+1]:
            coin += cash // coin_prices[day]
            cash -= coin * coin_prices[day]

    # print(day+1, cash, coin)

print(cash)