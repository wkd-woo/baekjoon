from sys import stdin

# 좌표평면 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

input = stdin.readline


def dfs(x, y, cnt):
    global ans
    ans = max(cnt, ans)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 그래프 범위에서 벗어나면 생략함
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue

        if (0 <= nx < r and 0 <= ny < c) and not graph[nx][ny] in passed:
            passed.add(graph[nx][ny])
            dfs(nx, ny, cnt + 1)
            passed.remove(graph[nx][ny])


r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]
passed = set()

ans = 0
passed.add(graph[0][0])
dfs(0, 0, 1)
print(ans)
