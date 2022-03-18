from collections import deque
from sys import stdin

input = stdin.readline

t = int(input())

# 좌표평면 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]  # 상하좌우 돌면서 확인
            ny = y + dy[i]

            # 그래프 범위에서 벗어나면 생략함
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 현 위치에서 그래프 값이 1이면
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))  # 0으로 초기화, 현 위치 좌표를 queue에 추가
    return


for _ in range(t):
    field = 0
    n, m, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]

    # x, y좌표 입력
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)
                field += 1

    print(field)
