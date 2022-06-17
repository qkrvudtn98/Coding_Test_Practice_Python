# 표준 라이브러리 : 특정한 프로그래밍 안에서 자주 사용되는 표준 소스코드를 미리 구현해 놓은 라이브러리

# 1. 내장함수 : import 명령어 없이 바로 사용 가능한 함수
# eval() 함수 : 수학 수식이 "문자열 형식"으로 들어오면 해당 수식을 계산한 결과 반환
result = eval("(3+5)*7")
print(result)

# 2. itertools : 파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리
from itertools import permutations # 순열 예시
data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)

from itertools import combinations # 조합 예시
data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print(result)

from itertools import product # product : r개의 데이터를 뽑아 일렬로 나열(순열)을 계산 (원소 중복하여 뽑음)
data = ['A', 'B', 'C']
result = list(product(data, repeat=2)) # repeat = 2 (뽑고 싶은 데이터의 개수)
print(result)

from itertools import combinations_with_replacement # combinations_with_replacement : 반복가능한 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우 반환
data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))
print(result)

# 3. heapq : 힙 기능을 위해 제공하는 라이브러리
import heapq

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value) # 힙에 원소 삽입
    for i in range(len(h)):
        result.append(heapq.heappop(h)) # 힙에서 원소를 꺼냄
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

# 파이썬에서는 최대힙 (Max Heap)을 제공하지 않는다 → heapq 라이브러리를 사용하여 최대힙을 구현할 때는 원소의 부호를 임시로 변경하는 방식 사용

import heapq
def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result
result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

# 4. bisect : 이진탐색구현 라이브러리 ('정렬된 배열'에서 특정한 원소를 찾아야 할 때 매우 효과적으로 사용됨) / 시간복잡도 : O(logN)
# bisect_left(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
# bisect_right(a, x) : 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
from bisect import bisect_left, bisect_right
a = [1,2,4,4,8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a, 4, 4))
print(count_by_range(a, -1, 3))

# 5. collections : 유용한 자료구조 제공하는 라이브러리
# deque : 첫번째 원소 제거 - popleft() / 마지막 원소 제거 - pop() / 첫번째 인덱스에 원소 x 삽입 appendleft(x) / 마지막 인덱스에 원소 삽입 - append(x)
from collections import deque

data = deque([2, 3, 4])
data.appendleft(1) # deque의 첫번째 원소 1 삽입
data.append(5) # deque의 마지막 원소 5 삽입

print(data)
print(list(data))

# Counter : 등장 횟수를 세는 기능을 제공 (반복 가능한 객체가 등장하였을 때, 해당 객체 내부의 원소가 몇 번씩 등장하였는지를 알려준다)
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['red'])
print(counter['blue'])
print(counter['green'])
print(dict(counter))

# 6. math : 수학적 기능을 포함하고 있는 라이브러리 (sqrt : 제곱근 / gcd(a,b) : 최대공약수 / pi ...)

# iterable 객체 : 반복 가능한 객체 (리스트 / 사전 자료형 / 튜플 자료형)