# 재귀 함수 : 자기 자신을 호출하는 함수

# 팩토리얼 예제 (반복적으로 구현)
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# 팩토리얼 예제 (재귀적으로 구현)
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))

# 재귀함수로 구현했을 때, 코드가 더 간결함!