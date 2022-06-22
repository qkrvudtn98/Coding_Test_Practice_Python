n, k = map(int, input().split())

coin_set = []
for coin in range(n):
    coin_set.append(int(input()))
coin_set.sort(reverse=True)

count = 0
for i in range(len(coin_set)):
    if k >= coin_set[i]:
        num = k//coin_set[i]
        count += k//coin_set[i]
        k -= num*coin_set[i]
    else:
        continue
    if k <= 0:
        break

print(count)




