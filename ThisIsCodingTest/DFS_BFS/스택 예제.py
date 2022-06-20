# 스택을 이용할 때에는 append()와 pop() 메서드를 이용하면 스택 자료구조와 동일하기 동작
# 스택 : FILO | LIFO
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])