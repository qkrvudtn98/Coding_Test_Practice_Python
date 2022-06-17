# 맵의 가로, 세로 크기 설정
n, m = map(int, input().split())

# 열의 값 초기화
d = [[0]*m for _ in range(n)]

# 게임 캐릭터가 있는 칸의 좌표 (A, B)와 바라보는 방향 d 입력
x, y, direction = map(int, input().split())
# 현재 좌표 방문처리
d[x][y] = 1

# 맵 입력
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전했을 때 방향값 변경 함수
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
