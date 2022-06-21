# 사람 수 n 입력 받기
n = int(input())

# 인출 시간 입력
p = list(map(int, input().split()))
p.sort()

total = 0
for i in range(n):
    total += p[i] * (n-i)

print(total)
