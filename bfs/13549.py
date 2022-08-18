from collections import deque

MAX = 100001
n, k = map(int, input().split())
l = [0] * MAX


def bfs():
    q = deque([n])
    while q:
        now_pos = q.popleft()
        if now_pos == k:
            return l[now_pos]
        for next_pos in (now_pos * 2, now_pos - 1, now_pos + 1):
            if 0 <= next_pos < MAX and not l[next_pos]:  # 방문하지 않았다면
                if next_pos == now_pos * 2:
                    l[next_pos] = l[now_pos]
                else:
                    l[next_pos] = l[now_pos] + 1

                q.append(next_pos)

print(bfs())