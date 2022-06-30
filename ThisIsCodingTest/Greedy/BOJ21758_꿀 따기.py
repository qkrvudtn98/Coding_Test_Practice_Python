# 장소의 수 N 입력
n = int(input())

# 장소별 꿀을 딸 수 있는 양
quantity = list(map(int, input().split()))

# 꿀 양의 최댓값 구하는 로직
max_honey = 0
sum_honey = []
sum_honey.append(quantity[0])
for i in range(1,n):
    sum_honey.append(sum_honey[i-1] + quantity[i])

# 꿀통이 왼쪽 끝
for i in range(1, n-1):
    max_honey = max(max_honey, sum_honey[n-2] - quantity[i] + sum_honey[i-1] )
# 꿀통이 오른쪽 끝
for i in range(1, n-1):
    max_honey = max(max_honey, sum_honey[n-1] - quantity[0] - quantity[i] + sum_honey[n-1] - sum_honey[i])
# 꿀통이 가운데
for i in range(1, n-1):
    max_honey = max(max_honey, sum_honey[n-2] - quantity[0] + quantity[i])

print(max_honey)

# 로직은 맞는데 왜 안되는지 반드시 체크할 것!
# for box in range(len(quantity)):
#     if box == 0:
#         for i in range(1, n-1):
#             sum_honey.append(sum(quantity[:i])*2 + sum(quantity[i+1:n-1]))
#     elif box == n-1:
#         for j in range(1, n-1):
#             sum_honey.append(sum(quantity[1:i])+sum(quantity[i+1:n])*2)
#     else:
#         sum_honey.append(sum(quantity[1:n-1])+quantity[box])
#
# max_honey = max(sum_honey)
# print(max_honey)




