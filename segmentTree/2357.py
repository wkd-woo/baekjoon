import heapq
from sys import stdin

input = stdin.readline


def mergeMin(left, right):
    return min(left, right)


def mergeMax(left, right):
    return max(left, right)


def buildMin(minTree, node, left, right):
    # leaf node
    if left == right:
        minTree[node] = l[left]
        return minTree[node]

    mid = left + (right - left) // 2
    left_val = buildMin(minTree, 2 * node, left, mid)
    right_val = buildMin(minTree, 2 * node + 1, mid + 1, right)
    minTree[node] = mergeMin(left_val, right_val)
    return minTree[node]


def buildMax(maxTree, node, left, right):
    # leaf node
    if left == right:
        maxTree[node] = l[left]
        return maxTree[node]

    mid = left + (right - left) // 2
    left_val = buildMax(maxTree, 2 * node, left, mid)
    right_val = buildMax(maxTree, 2 * node + 1, mid + 1, right)
    maxTree[node] = mergeMax(left_val, right_val)
    return maxTree[node]


def queryMin(start, end, node, left, right):
    if end < left or start > right:
        return int(1e9)

    if start <= left and right <= end:
        return minTree[node]

    mid = left + (right - left) // 2
    left_val = queryMin(start, end, 2 * node, left, mid)
    right_val = queryMin(start, end, 2 * node + 1, mid + 1, right)
    return mergeMin(left_val, right_val)


def queryMax(start, end, node, left, right):
    if end < left or start > right:
        return 1

    if start <= left and right <= end:
        return maxTree[node]

    mid = left + (right - left) // 2
    left_val = queryMax(start, end, 2 * node, left, mid)
    right_val = queryMax(start, end, 2 * node + 1, mid + 1, right)
    return mergeMax(left_val, right_val)


n, m = map(int, input().split())
l = [int(input()) for _ in range(n)]
minTree = [0 for _ in range(4 * len(l))]
maxTree = [0 for _ in range(4 * len(l))]
buildMax(maxTree, 1, 0, len(l) - 1)
buildMin(minTree, 1, 0, len(l) - 1)
for _ in range(m):
    a, b = map(int, input().split())
    print(queryMin(a-1, b-1, 1, 0, len(l) - 1),
          queryMax(a-1, b-1, 1, 0, len(l) - 1))
