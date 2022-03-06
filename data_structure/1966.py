from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    priority = deque(map(int, input().split()))
    index = deque(i for i in range(n))
    index[m] = 'target'    # 내가 찾고 싶은 index
    cnt = 0

    while priority:
        if priority[0] == max(priority):    # 나머지 문서들보다 중요도가 더 높은 문서가 없다면
            cnt += 1
            if index[0] == 'target':
                print(cnt)
                break
            priority.popleft()
            index.popleft()
        else:
            priority.append(priority.popleft())
            index.append(index.popleft())