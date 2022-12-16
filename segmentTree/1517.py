from sys import stdin
from collections import deque


input = stdin.readline


def merge(left, right):
    global cnt
    if left > right:
        cnt += 1
    return min(left, right)


def build(stree, node, left, right):
    # leaf node
    if left == right:
        stree[node] = l[left]
        return stree[node]

    mid = left + (right - left) // 2
    left_val = build(stree, 2 * node, left, mid)  # 왼쪽 자식의 최소
    right_val = build(stree, 2 * node + 1, mid + 1, right)  # 오른쪽 자식의 최소
    stree[node] = merge(left_val, right_val)
    return stree[node]


n = int(input())
l = list(map(int, input().split()))
stree = [0 for _ in range(4 * len(l))]
cnt = 0
build(stree, 1, 0, len(l) - 1)
print(stree)
print(cnt)
