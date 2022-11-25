from sys import stdin

input = stdin.readline

v, start, end, e = map(int, input().split())

INF = -int(1e9)
distances = [INF] * (v+1)
edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

l = list(map(int, input().split()))


def bellman_ford(start):
    distances[start] = 0  # 시작 노드에 대해서 초기화

    # 전체 v - 1 번의 라운드(round) 반복
    for i in range(v):
        for j in range(e):  # 매 반복마다 모든 간선을 확인
            cur = edges[j][0]
            next_ = edges[j][1]
            cost = edges[j][2]
            # 현재간선을 거쳐서 다음 노드로 이동하는 거리가 더 짧은 경우
            if distances[cur] != INF and distances[next_] < distances[cur] + cost:
                distances[next_] = distances[cur] + cost
                # v 번째 라운드에서도 값 갱신 -> 순환이 존재
                if i == v-1:
                    return True

    return False  # 순환 존재 X


# 벨만포드
cycle = bellman_ford(start)

print(distances)
print(distances[end])
