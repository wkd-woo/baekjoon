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


n, m = map(int, input().split())
l = [int(input()) for _ in range(n)]
stree = [0 for _ in range(4 * len(l))]
build(stree, 1, 0, len(l) - 1)
for _ in range(m):
    a, b = map(int, input().split())
    print(query(a-1, b-1, 1, 0, len(l) - 1))
