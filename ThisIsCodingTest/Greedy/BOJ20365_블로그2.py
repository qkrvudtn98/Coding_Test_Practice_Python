# 문제의 수 n 입력 받기
n = int(input())

# n개의 문자열 입력 받기
string = input()

# string을 R,B를 기준으로 각각 분리 후 변수에 저장
blue_num = string.split('B')
red_num = string.split('R')

# R, B의 개수 구하는 로직
count_r = 0
count_b = 0

for i in blue_num:
    if i != '':
        count_r += 1
for i in red_num:
    if i != '':
        count_b += 1

# R,B로 이루어진 문자열이 번갈아가며 연속됨 -> (개수가 더 적은 것 + 1)번 색칠하는 것이 최솟값
if count_r > count_b:
    answer = count_b + 1
else:
    answer = count_r + 1

# 정답 출력
print(answer)
