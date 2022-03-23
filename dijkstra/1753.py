from sys import stdin
import heapq

input = stdin.readline

INF = int(1e9)


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, node = heapq.heappop(queue)

        if distance[node] < dist:
            continue

        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(queue, (cost, next[0]))


v, e = map(int, input().split())
start = int(input())

graph = [[] for i in range(v + 1)]
visited = [False] * (v + 1)
distance = [INF] * (v + 1)

for _ in range(e):
    a, b, w = map(int, input().split())
    graph[a].append([b, w])

dijkstra(start)

for i in range(1, v + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])