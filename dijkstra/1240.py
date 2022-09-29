from collections import defaultdict
import heapq

INF = int(1e9)

n, m = map(int, input().split())
tree = defaultdict(list)
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    tree[u].append([v, w])
    tree[v].append([u, w])


def dijkstra(graph, start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance = [INF] * (n + 1)
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

    return distance


for _ in range(m):
    start, end = map(int, input().split())
    temp = dijkstra(tree, start)
    print(temp[end])
