# A B 값 입력
a, b = map(int, input().split())

# 출력값 찾는 로직
count = 1
while True:
    if a == b:
        break
    elif a > b or (b%10 != 1 and b%2 != 0):
        count = -1
        break
    elif b % 2 == 1:
        b = int((b-1)/10)
        count += 1
    elif b % 2 == 0:
        b = int(b/2)
        count += 1
print(count)

# [ 틀린 풀이 ]
# 틀린 이유 : 모든 반례를 고려해주지 않았다. a가 b보다 작아지는 경우에 대한 반례만 고려하고, 일의 자리 숫자가 1이 아닌데 2로 나누어지지 않는 홀수의 경우는 고려해주지 않았다. 나머지 로직들은 맞았다.

# # 연산 종류 정의
# # 2로 나누는 연산
# def divide(n):
#     return int(n/2)
# # 1을 떼는 연산
# def add(n):
#     return int((n-1)/10)
#
# # 출력값 찾는 로직
# count = 1
# while True:
#     if b % 2 == 1:
#         b = add(b)
#         count += 1
#         if b == a:
#             break
#         elif b < a:
#             count = -1
#             break
#         else:
#             continue
#
#     elif b % 2 == 0:
#         b = divide(b)
#         count += 1
#         if b == a:
#             break
#         elif b < a:
#             count = -1
#             break
#         else:
#             continue
#
# print(count)
