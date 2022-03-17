from collections import deque
from sys import stdin

input = stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q.append([x, y])
    temp[x][y] = cnt

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == graph[x][y] and temp[nx][ny] == 0:
                    q.append([nx, ny])
                    temp[nx][ny] = 1


n = int(input())
graph = [list(map(str, input())) for _ in range(n)]
temp = [[0] * n for _ in range(n)]
q = deque()

cnt = 0
for i in range(n):
    for j in range(n):
        if temp[i][j] == 0:
            bfs(i, j)
            cnt += 1

print(cnt, end=' ')

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

temp = [[0] * n for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(n):
        if temp[i][j] == 0:
            bfs(i, j)
            cnt += 1

print(cnt)
