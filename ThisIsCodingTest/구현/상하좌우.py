# 문제 : 상하좌우
# [문제설명]
# 여행가A는 N X N 크기의 정사각형 공간 위에 서 있다. 이 공간은 1 X 1 크기의 정사각형으로 나누어져 있다. 가장 왼쪽 위 좌표 (1,1) 가장 오른쪽 아래 좌표 (N,N)이다.
# 여행가A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1,1)이다.
# L : 왼쪽으로 한 칸 이동
# R : 오른쪽으로 한 칸 이동
# U : 위로 한 칸 이동
# D : 아래로 한 칸 이동

# [입력조건]
# 첫째 줄에 공간의 크기를 나타내는 N이 주어진다. (1<=N<=100)
# 둘째 줄에 여행가A가 이동할 계획서 내용이 주어진다. (1<=이동횟수<=100)

# [출력조건]
# 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (X,Y)를 공백으로 구분하여 출력한다.

# [문제풀이]
n = int(input()) # 좌표평면의 행&열 개수 입력
x, y = 1, 1 # 시작좌표 설정 (1,1)
plans = input().split() # 계획표 입력

dx = [0, 0, -1, 1] # 움직이는 x, y좌표 설정
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D'] # 움직임의 종류 (상하좌우)

for plan in plans:
    for i in range(len(move_types)): # move_type에 저장되어있는 타입 돌면서 검사
        if plan == move_types[i]: # plan의 타입와 일치하면 해당 x, y좌표를 옮겨주면 됨 (nx, ny는 현재 위치를 의미)
            nx = x + dx[i]
            ny = y + dy[i]
    if nx<1 or ny<1 or nx>n or ny>n: # 시작 좌표인 1보다 작아지거나, 설정한 행열의 길이보다 길어지면 continue
        continue
    x, y = nx, ny # 타입 검사 한 번 진행할 때마다 x, y 좌표에 반영

print(x,y)