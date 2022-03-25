import sys
from heapq import heappush, heappop

input = sys.stdin.readline

# 좌표평면 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

visit = [[0] * n for _ in range(n)]


def dijkstra():
    heap = []
    heappush(heap, [0, 0, 0])
    visit[0][0] = 1

    while heap:
        a, x, y = heappop(heap)
        if x == n - 1 and y == n - 1:
            print(a)
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 그래프 범위에서 벗어나면 생략함
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if visit[nx][ny] == 0:
                visit[nx][ny] = 1
                if graph[nx][ny] == 0:
                    heappush(heap, [a + 1, nx, ny])
                else:
                    heappush(heap, [a, nx, ny])

dijkstra()