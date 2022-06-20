n = int(input())

price = []
for _ in range(n):
    price.append(int(input()))

price.sort(reverse=True)
sum_price = 0
for i in range(len(price)):
    if (i%3 != 2):
        sum_price += price[i]

print(sum_price)