from heapq import heappop, heappush
from sys import stdin

# input = stdin.readline

INF = int(1e9)


def dijkstra(start):
    distance = [INF] * (n + 1)
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

    return distance


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for i in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])

    k = int(input())
    starts = list(map(int, input().split()))

    result = [0] * (n + 1)

    for start in starts:
        result = [i + j for i, j in zip(result, dijkstra(start))]

    print(result.index(min(result)))
