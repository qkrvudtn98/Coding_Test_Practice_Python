# 문제의 수 n 입력 받기
n = int(input())

# n개의 문자열 입력 받기
string = input()

# string을 R,B를 기준으로 분리
blue_num = string.split('B')
red_num = string.split('R')

count_r = 0
count_b = 0

for i in blue_num:
    if i != '':
        count_r += 1
for i in red_num:
    if i != '':
        count_b += 1

if count_r > count_b:
    answer = count_b + 1
else:
    answer = count_r + 1

print(answer)
