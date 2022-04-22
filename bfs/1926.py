from collections import deque


def bfs(x, y):
    # 좌표평면
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    cnt = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]  # 돌면서 확인
            ny = y + dy[i]

            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue

            # 현 위치에서 그래프 값이 1이면
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append([nx, ny])
                cnt += 1

    global big
    big = max(big, cnt)
    return


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

paints = 0
big = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(i, j)
            paints += 1

print(paints)
print(big)
