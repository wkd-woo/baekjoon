import heapq
from sys import stdin

input = stdin.readline


def merge(left, right):
    return min(left, right)


def build(stree, node, left, right):
    # leaf node
    if left == right:
        stree[node] = l[left]
        return stree[node]

    mid = left + (right - left) // 2
    left_val = build(stree, 2 * node, left, mid)
    right_val = build(stree, 2 * node + 1, mid + 1, right)
    stree[node] = merge(left_val, right_val)
    return stree[node]


def update(idx, val, node, left, right):
    if idx < left or idx > right:
        return stree[node]

    if left == right:
        stree[node] = val
        return stree[node]

    mid = left + (right - left) // 2
    left_val = update(idx, val, 2*node, left, mid)
    right_val = update(idx, val, 2*node + 1, mid + 1, right)
    stree[node] = merge(left_val, right_val)
    return stree[node]


def query(start, end, node, left, right):
    if end < left or start > right:
        return int(1e9)

    if start <= left and right <= end:
        return stree[node]

    mid = left + (right - left) // 2
    left_val = query(start, end, 2 * node, left, mid)
    right_val = query(start, end, 2 * node + 1, mid + 1, right)
    return merge(left_val, right_val)


n = int(input())
l = list(map(int, input().split()))
stree = [0 for _ in range(4 * len(l))]
build(stree, 1, 0, len(l) - 1)
m = int(input())
result = []
for _ in range(m):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        update(cmd[1]-1, cmd[2], 1, 0, n-1)
    else:
        i, j = min(cmd[1]-1, cmd[2]-1),  max(cmd[1]-1, cmd[2]-1)
        result.append(query(i, j, 1, 0, n-1))


for each in result:
    print(each)
