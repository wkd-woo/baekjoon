from sys import stdin
from collections import deque


input = stdin.readline


def merge(left, right):
    return min(left, right)


def build(stree, node, left, right):
    global result

    # leaf node
    if left == right:
        stree[node] = l[left]
        return stree[node]

    mid = left + (right - left) // 2
    left_val = build(stree, 2 * node, left, mid)  # 왼쪽 자식의 최소
    right_val = build(stree, 2 * node + 1, mid + 1, right)  # 오른쪽 자식의 최소
    result = max(result, left_val * abs(mid - left + 1),
                 right_val * abs(right - mid), min(left_val, right_val) * abs(right - left + 1))

    stree[node] = merge(left_val, right_val)
    return stree[node]


n = int(input())
l = [int(input()) for _ in range(n)]
stree = [0 for _ in range(4 * len(l))]
global result
result = max(min(l) * len(l), max(l))
build(stree, 1, 0, len(l) - 1)
print(result)


# stack[0] 이상이 될 때마다 인덱스랑 같이 스택을 쌓음
stack = deque()
result = max(max(l), min(l) * len(l))
for i in range(n):
    x = l[i]
    if not stack or stack[0][0] >= x:
        stack.append((x, i))  # (수, 인덱스) 형태로 삽입
    else:
        while stack:
            previous, index = stack.popleft()
            if stack:
                result = max(result, min(stack) * len(stack))
            if previous >= x:  # 이전 수가 현재 수보다 크다면
                stack.appendleft((previous, index))  # 다시 스택에 넣음
                break
        stack.append((x, i))  # (수, 인덱스) 형태로 삽입

print(result)
