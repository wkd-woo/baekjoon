from collections import deque
from sys import stdin

input = stdin.readline

t = int(input())

# 체스 좌표평면
dx = [1, -1, 1, -1, 2, 2, -2, -2]
dy = [2, 2, -2, -2, 1, -1, 1, -1]

for _ in range(t):
    l = int(input())
    graph = [[0] * l for _ in range(l)]

    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))

    queue = deque()
    queue.append(start)

    while queue:

        if start == end:
            break

        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]  # 상하좌우 돌면서 확인
            ny = y + dy[i]

            # 그래프 범위에서 벗어나면 생략함
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue

            # 현 위치에서 그래프 값이 0이면
            if graph[nx][ny] == 0:
                queue.append((nx, ny))  # 현 위치 좌표를 queue에 추가
                graph[nx][ny] = graph[x][y] + 1

    print(graph[end[0]][end[1]])
