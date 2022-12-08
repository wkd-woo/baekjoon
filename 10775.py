import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def find(v):
    if parent[v] == v:
        return v

    parent[v] = find(parent[v])
    return parent[v]


g = int(input())
p = int(input())
l = [int(input()) for _ in range(p)]
parent = [i for i in range(g+1)]
answer = 0
for plane in l:
    gate = find(plane)
    if gate == 0:
        break

    parent[gate] = gate - 1
    answer += 1

print(answer)
