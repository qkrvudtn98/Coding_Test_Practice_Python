# 회의 개수 입력
n = int(input())
# 회의 시작시간 종료시간 입력
group = []
for _ in range(n):
    start, end = map(int, input().split())
    group.append([start, end])

# 회의 시작시간에 대한 오름차순 적용
# 회의 종료시간에 대한 오름차순 적용
group = sorted(group, key=lambda a:a[0])
group = sorted(group, key=lambda a:a[1])

# group객체를 순회하며 카운트 값 반환
last = 0
count = 0
# group객체의 시작시간, 종료시간 각각 접근
for i, j in group:
    # 시작시간이 종료시간보다 늦을 경우
    if i >= last:
        # 회의 배정
        count += 1
        # 회의 종료시각 다음 회의의 종료시각으로 변경
        last = j

print(count)