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


n, m, x = map(int, input().split())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

result = []
for i in range(1, n + 1):
    temp = 0
    distance = [INF] * (n + 1)
    dijkstra(i)
    temp += distance[x]
    distance = [INF] * (n + 1)
    dijkstra(x)
    temp += distance[i]
    result.append(temp)

print(max(result))
