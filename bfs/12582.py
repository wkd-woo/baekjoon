from collections import deque

MAX = 1000001
n = int(input())
l = [0] * (MAX+1)
path = [[i] for i in range(MAX+1)]


def bfs():
    q = deque([n])
    while q:
        now_pos = q.popleft()
        if now_pos <= 1:
            return

        next_ = []
        if now_pos % 3 == 0:
            next_.append(now_pos//3)
        if now_pos % 2 == 0:
            next_.append(now_pos//2)
        next_.append(now_pos-1)
        for next_pos in next_:
            if 0 <= next_pos < MAX:
                if not l[next_pos]:  # 방문하지 않았다면
                    l[next_pos] = l[now_pos] + 1
                    path[next_pos].extend(path[now_pos])
                    q.append(next_pos)
                elif l[next_pos] == l[now_pos] + 1:
                    q.append(next_pos)

    return


result = bfs()
print(l[1])
print(*reversed(path[1]))
