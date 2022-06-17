# 거스름돈 문제
n = 1260
count = 0
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)

# 시간복잡도 : O(K)
# 거스름돈 문제에서는 항상 큰 단위가 작은 단위의 배수 형태이므로, 최적의 해를 보장할 수 있는 것임!
# 큰 단위가 작은 단위의 배수가 아니라면, 다이나믹 프로그래밍이나 그래프 알고리즘으로 해결!
