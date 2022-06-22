# 운동기구 입력
n = int(input())

# 각 운동기구별 근손실 값 입력
t = list(map(int, input().split()))
t.sort(reverse=True)

result = []

if len(t)%2==1:
    result.append(t[0])
    t.pop(0)

for i in range(len(t)//2):
    result.append(t[i] + t[len(t)-i-1])

print(max(result))



