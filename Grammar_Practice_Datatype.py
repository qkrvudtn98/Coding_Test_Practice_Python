# 수 자료형 => 코딩 테스트에서는 대부분의 경우 정수형을 다루는 문제가 출제 ( 실수형을 다루는 문제는 출제 빈도↓ )

# 정수형 : 양의 정수 / 음의 정수 / 0
a = 1000
print(a)

a = -7 #양의 정수
print(a)

a = 0 #음의 정수
print(a)

# 실수형 : 변수에 소수점을 붙인 수를 대입하면 실수형 변수로 처리 ( 소수부가 0이거나 정수부가 0인 소수는 0을 생략하고 작성할 수 있다 )
# 실수형 데이터 표현 방식 : e 또는 E 사용하여 지수 표현 ( Ex : 1e9 = 10**9 )
a = 1e9
print(a) # 1 * (10**9)

a = 75.25e1
print(a) # 75.25 * (10**1)

a = 3954e-3
print(a) # 3954 * (10**-3)

# 실수 처리 : 부동 소수점 (Floating-point)방식으로 처리하는데 4 또는 8 바이트의 수로 표현하기 때문에 정확도에 한계를 가진다
# → 코딩테스트에서는 실수를 처리할 때 소숫점 다섯번째 자리에서 반올림한 결과가 일치하면 정답으로 처리함

# 리스트 자료형 ( = 배열 / 테이블 )
# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화 ( 코딩테스트에서 많이 사용 )
n = 10
a = [0] * n
print(a)

# 리스트의 인덱싱과 슬라이싱
# 인덱싱 : 리스트의 원소들에 접근 / 슬라이싱 : 리스트의 일정 범위들 반환

# 리스트 컴프리헨션 (리스트 초기화 방법)
# 대괄호 안에 조건문 & 반복문 넣어서 리스트 초기화
# 1차원 배열 초기화
array = [i for i in range(20) if i % 2 == 1] # 홀수만 뽑아서 초기화시키는 리스트
print(array)

array = [i*i for i in range(1,10)]
print(array)

# 2차원 배열 초기화 (N X M)
n = 3
m = 4
array = [[0]*m for _ in range(n)] # 언더바(_) : 반복을 수행하지만 반복을 위한 변수의 값을 무시하고 싶을 때 _ 사용
array[1][1] = 5
print(array)

# N X M 크기의 2차원 리스트 초기화 (잘못된 방법)
n = 3
m = 4
array = [[0]*m]*n
print(array)

array[1][1] = 5 # 내부적으로 포함된 3개의 레퍼런스가 모두 동일한 객체에 대한 3개의 레퍼런스로 인식
print(array)

# → 2차원 리스트 초기화 할 때는 리스트 컴프리헨션을 이용해주어야 함

# 리스트 관련 기타 메서드
# append() : O(1) / sort() : O(NlogN) / reverse() : O(N) / insert() : O(N) / count() : O(N) / remove() : O(N)

# 특정 값의 원소를 모두 제거하는 방법
a = [1,2,3,4,5,5,5]
remove_set = [3,5]

result = [i for i in a if i not in remove_set]
print(result)

# 튜플 자료형 : 튜플은 한 번 선언된 값을 변경할 수 없다 / 소괄호 이용
a = (1,2,3,4)
print(a)

# a[2] = 7
# print(a)
# 튜플은 그래프 알고리즘에 자주 사용됨
# 튜플의 장점 : 1. 변경하면 안되는 값이 변경되고 있지는 않은지 체크할 수 있음 / 2. 리스트에 비해 공간 효율적 / 3. 각 원소의 성질이 다를 때 주로 사용

# 사전 자료형
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

key_list = data.keys() # keys : 키 값만 뽑아내는 함수
value_list = data.values() # values : 값 데이터만 뽑아내는 함수
print(key_list)
print(value_list)

for key in key_list :
    print(data[key])

# 집합 자료형 : 중복 허용 x / 순서 x
# 리스트 & 튜플 과의 차이점 : 순서가 없기 때문에 인덱싱 불가능  / 시간 복잡도 : O(1)

# 집합 자료형 초기화 방법1 : set 함수 사용
data = set([1,1,2,3,4,4,5])
print(data)

# 집합 자료형 초기화 방법2 : {} 중괄호 이용
data = {1,1,2,3,4,4,5}
print(data)

# 집합 자료형의 연산 : 합집합 (|) / 교집합 (&) / 차집합 (-)
a = set([1,2,3,4,5])
b = set([3,4,5,6,7])

print(a|b)
print(a&b)
print(a-b)

# 집합 자료형 관련 함수 (모두 시간복잡도 O(1))
# add() : 하나의 집합 데이터에 값을 추가
# update() : 여러 개의 집합 데이터를 추가
# remove() : 특정한 값을 제거
