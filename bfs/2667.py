from collections import deque

# 좌표평면 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, x, y):
    n = len(graph)
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]  # 상하좌우 돌면서 확인
            ny = y + dy[i]

            # 그래프 범위에서 벗어나면 생략함
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            # 현 위치에서 그래프 값이 1이면
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))  # 0으로 초기화, 현 위치 좌표를 queue에 추가
                cnt += 1

    return cnt


n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, list(input()))))

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(graph, i, j))

print(len(result))
print(*sorted(result), sep='\n')