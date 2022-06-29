n = input()

max_num = []
min_num = []
mk_num = n.split('K')

for m in mk_num:
    if m :
        min_num.append(str(10**(len(m)-1)))
        max_num.append(str(5*10**(len(m))))
    else:
        min_num.append('')
        max_num.append(str(5))

# max_num의 마지막에 M이 들어올 경우 1이 나와야하는데 문제 특성상 50이 나오게 됨 => 50을 제거하고 1을 추가하는 로직 작성
max_result = "".join(max_num[:-1]) + '1'*(len(max_num[-1])-1)
min_result = "5".join(min_num)

print(max_result + '\n' + min_result)