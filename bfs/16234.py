import copy
import sys
from collections import deque

sys.setrecursionlimit(10 ** 5)

# 좌표평면 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    temp = [(x, y)]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]  # 상하좌우 돌면서 확인
            ny = y + dy[i]

            # 그래프 범위에서 벗어나면 생략함
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            diff = abs(graph[nx][ny] - graph[x][y])

            # 차이가 l이상 r 이하이고 방문하지 않았다면
            if l <= diff <= r and not visit[nx][ny]:
                visit[nx][ny] = 1
                queue.append((nx, ny))  # 현 위치 좌표를 queue에 추가
                temp.append((nx, ny))
    return temp


n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
before = copy.deepcopy(graph)

cnt = 0
while True:
    visit = [[0] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                visit[i][j] = 1
                temp = bfs(i, j)
                if len(temp) > 1:
                    num = sum([graph[x][y] for x, y in temp]) // len(temp)
                    for x, y in temp:
                        graph[x][y] = num

    if before != graph:
        cnt += 1
        before = copy.deepcopy(graph)
    else:
        break

print(cnt)
