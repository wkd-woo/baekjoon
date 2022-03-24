from heapq import heappop, heappush
from sys import stdin

input = stdin.readline

INF = int(1e9)


def dijkstra(start):
    heap = []
    distance[start] = 0
    heappush(heap, (0, start))

    while heap:
        dist, now = heappop(heap)
        if distance[now] < dist:
            continue

        for next, next_cost in graph[now]:
            cost = dist + next_cost
            if cost < distance[next]:
                distance[next] = cost
                heappush(heap, (cost, next))


t = int(input())

for _ in range(t):
    n, d, c = map(int, input().split())

    graph = [[] for i in range(n + 1)]
    visited = [False] * (n + 1)
    distance = [INF] * (n + 1)

    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append([a, s])

    dijkstra(c)
    result = [item for item in distance if item != INF]
    print(len(result), max(result))
