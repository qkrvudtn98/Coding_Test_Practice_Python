rope_num = int(input())
weight = []
value = []
for _ in range(rope_num):
    max_value = int(input())
    weight.append(max_value)

weight.sort(reverse=True)

for j in range(rope_num):
    value.append(weight[j]*(j+1))

print(max(value))

