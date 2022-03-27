from sys import stdin
from heapq import heappop, heappush

input = stdin.readline

INF = int(1e9)


def dijkstra(start):
    queue = []
    heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, node = heappop(queue)

        if distance[node] < dist:
            continue

        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heappush(queue, (cost, next[0]))


n, d = map(int, input().split())

graph = [[] for i in range(d + 1)]
distance = [INF] * (d + 1)

for i in range(d):
    graph[i].append((i + 1, 1))  # 노드마다 cost 정해주는것이 핵심

for _ in range(n):
    start, end, length = map(int, input().split())
    if end > d: continue

    graph[start].append([end, length])

dijkstra(0)
print(distance[d])
