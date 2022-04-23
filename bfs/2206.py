from collections import deque
from sys import stdin

input = stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, stdin.readline().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque()
    queue.append([0, 0, 1])
    visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visit[0][0][1] = 1

    while queue:
        x, y, w = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visit[x][y][w]
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < m:
                if graph[xx][yy] == 1 and w == 1:
                    visit[xx][yy][0] = visit[x][y][w] + 1
                    queue.append([xx, yy, 0])
                elif graph[xx][yy] == 0 and visit[xx][yy][w] == 0:
                    visit[xx][yy][w] = visit[x][y][w] + 1
                    queue.append([xx, yy, w])
    return -1


print(bfs())







