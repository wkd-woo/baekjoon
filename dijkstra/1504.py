import sys
from heapq import *

input = sys.stdin.readline

INF = int(1e9)

n, e = map(int, input().split())
distance = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start):
    heap = []
    distance[start] = 0
    heappush(heap, (0, start))
    while heap:
        dist, now = heappop(heap)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(heap, (cost, i[0]))


v1, v2 = map(int, input().split())

dijkstra(1)
s1, s2 = distance[v1], distance[v2]

distance = [INF] * (n + 1)
dijkstra(v1)
u, a1 = distance[v2], distance[n]

distance = [INF] * (n + 1)
dijkstra(v2)
a2 = distance[n]

f = min(s1 + u + a2, s2 + u + a1)
print(f if f < INF else -1)
