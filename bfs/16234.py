from collections import deque

# 좌표평면 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    global border
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]  # 상하좌우 돌면서 확인
            ny = y + dy[i]

            # 그래프 범위에서 벗어나면 생략함
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            diff = abs(graph[nx][ny] - graph[x][y])

            # 현 위치에서 그래프 값이 1이면
            if l <= diff <= r and not border[nx][ny]:
                border[x][y] = 1
                border[nx][ny] = 1
                queue.append((nx, ny))  # 0으로 초기화, 현 위치 좌표를 queue에 추가


n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
border = [[0] * n for _ in range(n)]

cnt = 0
while True:

    for i in range(n):
        for j in range(n):
            bfs(i, j)

    mod = 0
    nation = 0
    queue = deque()
    for i in range(n):
        for j in range(n):
            if border[i][j]:
                queue.append((i, j))
                mod += graph[i][j]
                nation += 1

    if nation != 0:
        cnt += 1
        mod = mod // nation

        while queue:
            i, j = queue.popleft()
            graph[i][j] = mod
    else:
        break

print(cnt)
