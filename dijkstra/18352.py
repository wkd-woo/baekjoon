import heapq
from sys import stdin

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


n, m, k, start = map(int, input().split())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append([b, 1])

dijkstra(start)

result = []
for i in range(1, n + 1):
    if distance[i] == k:
        result.append(i)

if not result:
    print(-1)
else:
    for each in result:
        print(each)