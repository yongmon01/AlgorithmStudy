n, m = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

d = [10001] * 10001
for coin in coins:
    d[coin] = 1

for coin in coins:
    for i in range(coin, 10001-coin):
        if d[i] != 10001:
            d[i + coin] = min(d[i] + 1, d[i + coin])

print(d[:18])
if d[m] != 10001:
    print(d[m])
else:
    print(-1)