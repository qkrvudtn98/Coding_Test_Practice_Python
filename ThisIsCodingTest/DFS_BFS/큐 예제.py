# 큐 : 먼저 들어간 데이터 먼저 나옴 / 나중에 들어간 데이터 나중에 나옴 (FIFO)
# 큐 구현을 위해 deque 라이브러리 사용
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

# 큐 구현에서는 collections 모듈에서 지원하는 deque 자료구조를 활용
# deque는 스택 + 큐 장점 합친 것 -> 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적 + queue 라이브러리를 이용하는 것보다 간단함
# deque객체를 리스트 자료형으로 변경하고자 한다면 list(queue)를 하면 됨