# 테스트 케이스 개수 입력
t = int(input())

# 테스트 케이스 개수만큼 신입사원 성적 입력
score = []
count_one = []
count_two = []
count = 0
result = []
for i in range(t):
    # 테스트 케이스 입력
    n = int(input())
    [score.append(list(map(int, input().split()))) for j in range(n)]
    # 1차 시험 기준 정렬 / 2차 시험 기준 정렬
    one = sorted(score, key=lambda x : x[0])
    two = sorted(score, key=lambda x : x[1])

    count_one.append(one[0])
    count_two.append(two[0])

    for j in range(1,n):
        if one[j][1] < one[0][1]:
            count_one.append(one[j])
        if two[j][0] < two[0][0]:
            count_two.append(two[j])

    for k in range(len(count_one)):
        for j in range(len(count_two)):
            if count_one[k] == count_two[j]:
                count += 1
            else:
                continue

    result.append(count)

    # 테스트 케이스 종료 후 신입사원 성적 리스트 초기화
    score = []
    count_one = []
    count_two = []
    count = 0

for i in range(t):
    print(result[i])