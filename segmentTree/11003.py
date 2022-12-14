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
l = list(map(int, input().split()))
stree = [0 for _ in range(4 * n)]
build(stree, 1, 0, n-1)
d = []
for i in range(n):
    d.append(query(max(0, i - m + 1), i, 1, 0, n-1))

print(*d)
