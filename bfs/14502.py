import copy
from collections import deque
import sys

input = sys.stdin.readline

# 백트래킹 방식
 # - 모든 경우의 수를 해 본 뒤, 최대/최솟값 저장 - 탐색 후 출력

# 좌표평면 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


def bfs():
    queue = deque()

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:  # 바이러스(2)를 찾아서 queue에 저장
                queue.append((i, j))

    disaster = copy.deepcopy(graph)

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]  # 상하좌우 돌면서 확인
            ny = y + dy[i]

            # 그래프 범위에서 벗어나면 생략함
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 현 위치에서 그래프 값이 0이면
            if disaster[nx][ny] == 0:
                disaster[nx][ny] = 2  # 2로 변환
                queue.append((nx, ny))  # 현 위치 좌표를 queue에 추가

    # 전역변수 설정
    global answer
    cnt = 0

    for each in disaster:
        cnt += each.count(0)
    # 0 의 개수가 가장 많은 케이스 확인
    answer = max(answer, cnt)


def make_wall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(cnt + 1)
                graph[i][j] = 0


answer = 0
make_wall(0)
print(answer)
