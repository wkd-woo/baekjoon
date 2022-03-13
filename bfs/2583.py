from collections import deque

# 좌표평면 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 영역의 개수와, 각 영역의 넓이를 구해야 할 때
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]  # 상하좌우 돌면서 확인
            ny = y + dy[i]

            # 그래프 범위에서 벗어나면 생략함
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            # 현 위치에서 그래프 값이 1이면
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))  # 0으로 초기화, 현 위치 좌표를 queue에 추가
                cnt += 1

    return cnt


m, n, k = map(int, input().split())

graph = [[1] * n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 0

result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(i, j))

print(len(result))
print(*sorted(result), sep=' ')
