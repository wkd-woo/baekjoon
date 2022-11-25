import sys

input = sys.stdin.readline


INF = int(1e9)


def bellman_ford(start):
    distances[start] = 0  # 시작 노드에 대해서 초기화

    # 전체 v - 1 번의 라운드(round) 반복
    for i in range(v):
        for j in range(w + 2 * e):  # 매 반복마다 모든 간선을 확인
            cur = edges[j][0]
            next_ = edges[j][1]
            cost = edges[j][2]
            # 현재간선을 거쳐서 다음 노드로 이동하는 거리가 더 짧은 경우
            if distances[next_] > distances[cur] + cost:
                distances[next_] = distances[cur] + cost
                if i == v-1:
                    return True

    return False  # 음수 순환 존재 X


for _ in range(int(input())):
    v, e, w = map(int, input().split())

    edges = []
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        edges.append([a, b, c])
        edges.append([b, a, c])

    for _ in range(w):
        a, b, c = map(int, input().split())
        edges.append([a, b, -c])

    distances = [INF] * (v+1)
    result = bellman_ford(1)

    print("YES") if result else print("NO")
