from collections import deque


def bfs(start):
    cnt = 1
    queue = deque([start])
    visited = [0 for _ in range(n + 1)]
    visited[start] = 1

    while queue:
        node = queue.popleft()
        for each in graph[node]:
            if not visited[each]:
                queue.append(each)
                visited[each] = 1
                cnt += 1

    return cnt


n, m = map(int, input().split())

# 이차원 배열의 행을 정점 개수만큼
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    node_1, node_2 = map(int, input().split())
    graph[node_2].append(node_1)

result = []
for i in range(1, n + 1):
    result.append(bfs(i))

max_num = max(result)

for i in range(len(result)):
    if result[i] == max_num:
        print(i + 1, end=' ')
