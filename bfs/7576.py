from collections import deque

# 좌표평면 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]  # 상하좌우 돌면서 확인
            ny = y + dy[i]

            # 그래프 범위에서 벗어나면 생략함
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            # 현 위치에서 그래프 값이 0이면
            if graph[nx][ny] == 0:
                queue.append((nx, ny))  # 현 위치 좌표를 queue에 추가
                graph[nx][ny] = graph[x][y] + 1  # 직전 위치보다 1씩 증가시킴
    return


n, m = map(int, input().split())

graph = []
for _ in range(m):
    graph.append(list(map(int, list(input().split()))))

queue = deque([[i, j] for i in range(m) for j in range(n) if graph[i][j] == 1])

bfs()
result = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            print(-1)
            exit(0)
    result = max(result, max(graph[i]))

print(result - 1)