n = int(input())

quantity = list(map(int, input().split()))
quantity.sort()
total = max(quantity)

for i in range(n-1):
    total += (quantity[i]/2)

print(total)