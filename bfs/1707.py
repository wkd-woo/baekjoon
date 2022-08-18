from collections import deque


def bfs(start, group):
    q = deque([start])
    visited[start] = group

    while q:
        x = q.popleft()
        for i in graph[x]:  # x와 연결되어 있는 노드 중
            if not visited[i]:  # 방문하지 않았다면
                q.append(i)
                visited[i] = -1 * visited[x]  # x와 다른 그룹으로 방문처리
            elif visited[i] == visited[x]:  # 만약 같은 그룹으로 묶여 있다면
                return False  # False return

    return True  # 탐색이 끝났다면 True return


for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for i in range(v + 1)]
    visited = [False] * (v + 1)

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v + 1):
        if not visited[i]:  # 방문하지 않았다면
            result = bfs(i, 1)  # group 하여 bfs
            if not result:
                break

    print('YES' if result else 'NO')
