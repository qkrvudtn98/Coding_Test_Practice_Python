# 식 입력
expr = input().split('-')

# 최솟값을 저장할 변수 선언
result = 0

# 첫번째 원소는 무조건 더해주는 숫자임
for i in expr[0].split('+'):
    result += int(i)

# 두번째 원소부터는 무조건 -로 연결되므로 빼주는 알고리즘 작성
for i in expr[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)
