import sys
from heapq import heappush, heappop

input = sys.stdin.readline

INF = int(1e9)

# 좌표평면 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dijkstra():
    distance = [[INF] * n for _ in range(n)]
    heap = []
    heappush(heap, [graph[0][0], 0, 0])

    while heap:
        a, x, y = heappop(heap)
        if x == n - 1 and y == n - 1:
            print("Problem {0}: {1}".format(cnt, a))
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 그래프 범위에서 벗어나면 생략함
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            na = a + graph[nx][ny]
            if na < distance[nx][ny]:
                distance[nx][ny] = na
                heappush(heap, [na, nx, ny])


cnt = 0
while True:
    cnt += 1
    n = int(input())

    if not n: break

    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    visit = [[0] * n for _ in range(n)]
    dijkstra()