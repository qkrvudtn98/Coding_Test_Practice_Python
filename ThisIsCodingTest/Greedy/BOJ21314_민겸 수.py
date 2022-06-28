n = input()

# 최댓값 구하는 로직
max_num = []
max_count = 0
for i in range(len(n)):
    if n[i] == 'M' and n[i+1] == 'K':
        max_count += 1
        max_num.append(str(5*(10**max_count)))
        max_count = 0
    elif n[i] == 'K' and (n[i-1] =='K' or i==0):
        max_num.append('5')

# 최솟값 구하는 로직
min_num = []
min_count = 0
for i in range(len(n)):
    if n[i] == 'M' and i == len(n)-1:
        min_num.append('1')
    elif n[i] == 'M' and n[i+1] == 'K':
        min_count += 1
        min_num.append(str(10**(min_count-1)))
        min_count = 0
    elif n[i] == 'M' and n[i+1] != 'K':
        min_count += 1
    else:
        min_num.append('5')
min_result = ''.join(min_num)

