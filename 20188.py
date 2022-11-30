import heapq
from collections import defaultdict

INF = int(1e9)


n = int(input())
answer = 0
graph = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append([v, 1])
    graph[v].append([u, 1])

db = {i: [0] * (n+1) for i in range(1, n+1)}


def dijkstra(graph, start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance = [INF] * (n + 1)
    distance[start] = 0

    while queue:
        dist, node = heapq.heappop(queue)

        if distance[node] < dist:
            continue

        for next_ in graph[node]:
            cost = distance[node] + next_[1]
            if cost < distance[next_[0]]:
                distance[next_[0]] = cost
                heapq.heappush(queue, (cost, next_[0]))
                db[start][next_[0]] = 1
            elif cost == distance[next_[0]]:
                db[start][next_[0]] += 1

    return distance


answer = 0
for i in range(1, n+1):
    temp = 1
    dijkstra(graph, i)[1]
    temp * db[i][1]
    print(db[i])
    dijkstra(graph, i)
    answer += temp * sum(db[1][i:])

print(answer)
