# 테스트 케이스 숫자 입력
t = int(input())

# 지원자 점수 입력 리스트
recruit = []

# 점수 입력
for i in range(t):
    # 지원자 수 입력
    n = int(input())
    for j in range(n):
        recruit.append(list(map(int, input().split())))
    print(recruit)
    max_count = 0




