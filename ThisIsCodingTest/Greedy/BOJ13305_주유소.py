# 정답 풀이 (서브태스크 O)
n = int(input())

length = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = price[0]
sum_price = 0

for i in range(n-1):
    if(price[i] < min_price):
        min_price = price[i]

    sum_price += (min_price * length[i])

print(sum_price)

#--------------------------------------------------------

# 서브태스크 만족 못한 풀이
n = int(input())

length = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = price[0]
sum_length = 0
sum_price = []

for i in range(len(price)):
    if(price[i] <= min_price):
        sum_price.append(sum_length * min_price)
        if (i == len(length)):
            break
        min_price = price[i]
        sum_length = length[i]
    else:
        if(i == len(length)):
            break
        sum_length += length[i]

answer = 0
for j in range(len(sum_price)):
    answer += sum_price[j]

print(answer)