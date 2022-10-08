from collections import deque

MAX = 100001
n, k = map(int, input().split())
l = [0] * MAX
path = {n: -1}


def bfs():
    q = deque([n])
    while q:
        now_pos = q.popleft()
        if now_pos == k:
            return l[now_pos]

        if now_pos == 0:
            next_ = [now_pos + 1]
        else:
            next_ = [now_pos * 2, now_pos - 1, now_pos + 1]

        for next_pos in next_:
            if 0 <= next_pos < MAX and not l[next_pos]:  # 방문하지 않았다면
                if now_pos != 0 and next_pos == now_pos * 2:
                    l[next_pos] = l[now_pos] + 1
                    path[next_pos] = now_pos
                else:
                    l[next_pos] = l[now_pos] + 1
                    path[next_pos] = now_pos

                q.append(next_pos)


cnt = bfs()
print(cnt)
answer, pos = [], k
for _ in range(cnt):
    answer.append(pos)
    pos = path[pos]

answer.append(n)
answer.reverse()
print(*answer)
