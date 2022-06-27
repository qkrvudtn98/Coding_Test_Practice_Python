# 색을 칠해야 하는 문제의 수 입력
n = int(input())

# n개의 문자 공백없이 입력
result = input()
answer = []
if result[0] == 'B':
    for i in reversed(range(n)):
        answer.append(result[i])
else:
    for i in reversed(range(n)):
        answer.append(result[i])
