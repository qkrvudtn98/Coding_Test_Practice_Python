n = list(map(int, input().split()))

coin_types = [500, 100, 50, 10, 5, 1]
count = 0
target = 1000 - n[0]

for coin in coin_types:
    count += target // coin
    target %= coin

print(count)


