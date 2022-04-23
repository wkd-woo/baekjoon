from heapq import heappop, heappush

INF = int(1e9)


def dijkstra(start):
    heap = []
    distance = [INF] * (n + 1)
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


n = int(input())
graph = [[] for i in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

d2 = dijkstra(1)
print(max(dijkstra(d2.index(max(d2[1:])))[1:]))
