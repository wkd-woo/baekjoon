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
                path[next] = []
                for p in path[now]:
                    path[next].append(p)
                path[next].append(next)


n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

path = [[] * n for _ in range(n + 1)]
path[1].append(1)
dijkstra(1)

print(len(distance) - 2)
for each in path:
    if len(each) > 1:
        if len(each) > 2:
            print(*each[-2:])
        else:
            print(*each)