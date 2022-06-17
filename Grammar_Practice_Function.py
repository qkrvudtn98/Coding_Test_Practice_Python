# global 키워드로 변수 지정 → 해당 함수에서는 지역 변수를 만들지 않고 함수 바깥에 선언된 변수 바로 참조
a = 0
def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)

# 람다 표현식
print((lambda a, b: a+b)(4,5)) # 람다 표현식으로 add 메서드 구현 