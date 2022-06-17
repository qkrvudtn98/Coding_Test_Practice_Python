# 문제 : 1이 될 때까지
# [문제설명]
# 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행
# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다.

# [입력조건]
# 첫째 줄에 N(2<=N<=100000)과 K(2<=K<=100000)가 공백으로 구분되며 각각 자연수로 주어진다. 이때 입력으로 주어지는 N은 항상 K보다 크거나 같다.
# [출력조건]
# 첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력한다.

# [문제풀이]
# 단순하게 푸는 답안 예시
n, k = map(int, input().split())
result=0

while n>=k:
    if n%k != 0:
        n-=1
        result+=1
    n//=k
    result+=1

while n>1:
    n-=1
    result+=1

print(result)

# 효율적인 문제 풀이 예시
n, k = map(int, input().split())
result=0

while True:
    target=(n//k)*k
    result+=(n-target)
    n=target

    if n<k:
        break

    result+=1
    n//=k
result+=(n-1)
print(result)