n = int(input())

cash = []
for _ in range(n):
    cash.append(int(input()))
cash.sort(reverse=True)

tip = 0
for i in range(1,n+1):
    if(cash[i-1]-(i-1) >= 0):
        tip += cash[i-1]-(i-1)
    else:
        continue

print(tip)
