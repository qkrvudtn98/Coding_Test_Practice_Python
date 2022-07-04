import sys
# 테스트 케이스 개수 입력
t = int(input())

for i in range(t):
    score = []
    count = 1
    # 테스트 케이스 입력
    n = int(input())
    for j in range(n):
        paper, interview = map(int, sys.stdin.readline().split())
        score.append([paper, interview])

    score.sort()
    # 서류 1등의 면접 순위가 기준
    max_score = score[0][1]

    for j in range(1, n):
        if max_score > score[j][1]:
            count += 1
            max_score = score[j][1]

    print(count)