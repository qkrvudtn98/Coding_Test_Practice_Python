# N, M을 공백으로 구분하여 입력
n, m = map(int, input().split())

# 2차원 리스트 공간 입력
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# 상하좌우 탐색 + 방문처리하는 함수 구현
def dfs(x, y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False

    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j)==True:
            result+=1

print(result)