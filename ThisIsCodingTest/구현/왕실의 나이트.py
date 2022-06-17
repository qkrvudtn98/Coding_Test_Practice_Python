input_data = input() # 시작 좌표 입력
row = int(input_data[1]) # 행의 좌표 입력
column = int(ord(input_data[0])) - int(ord('a')) + 1 # 열의 좌표 입력 (문자로 입력받은 a~h 정수형으로 변환)

steps = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)] # 나이트가 움직일 수 있는 경우의 수

result = 0

for step in steps: # 나이트가 갈 수 있는 이동경로 검사
    next_xstep = row + step[0]
    next_ystep = column + step[1]
    # 겅로 하나씩 대입 → 문제에서 제공한 행열에서 벗어나는지 확인 후 안벗어나면 result+1
    if next_xstep >= 1 and next_ystep >= 1 and next_xstep <= 8 and next_ystep <= 8:
        result+=1

print(result)