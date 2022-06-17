# 입력을 위한 소스코드
# input() : 문자열을 입력받는 메서드 / int() : 문자열을 정수형으로 변환해주는 메서드 → int(input()) : 입력한 문자열을 정수형으로 바꿔주는 역할
# n = int(input()) # 데이터의 개수 입력
# data = list(map(int, input().split())) # 각 데이터를 공백으로 분리하여 입력
#
# data.sort(reverse=True) # 내림차순으로 정렬
# print(data)

# 공백을 기준으로 구분하여 적은 수의 데이터 입력
n, m, k = map(int, input().split())

print(n, m, k)
# 언어별로 입력을 빠르게 받고 있는 방법을 알고 있어야 함!

# 입력의 개수가 많은 경우에는 input() 함수를 사용하지 않고 sys.stdin.readline() 함수를 이용
import sys
data = sys.stdin.readline().rstrip()
print(data)
# sys 라이브러리를 사용할 때는 한 줄 입력을 받고나서 rstrip() 함수를 꼭 호출해야 함!
# readline()으로 입력하면 입력 후 엔터가 줄 바꿈 기호로 입력되는데, 이 공백문자를 제거하려면 rstrip() 함수를 사용해야함!

# 출력을 위한 소스코드 : print() 사용 