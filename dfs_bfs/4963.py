from sys import stdin
from collections import deque

input = stdin.readline


def bfs(x, y):
    # 좌표평면
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]  # 돌면서 확인
            ny = y + dy[i]

            # 현 위치에서 그래프 값이 1이면
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append([nx, ny])

    return


while True:
    w, h = map(int, input().split())
    if not w and not h:
        break

    graph = []
    cnt = 0

    for _ in range(h):
        graph.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)
