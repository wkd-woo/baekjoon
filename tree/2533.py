import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n = int(input())
graph = [[] for i in range(n + 1)]
tree = [[] for i in range(n + 1)]
parents = [i for i in range(n + 1)]
early = [False for i in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


# 그래프로 트리만들기
def makeTree(cur, parent):
    for node in graph[cur]:
        if node != parent:
            tree[cur].append(node)
            parents[node] = cur
            makeTree(node, cur)


makeTree(1, -1)


# 1. 연결된 노드가 하나밖에 없는 노드와 연결된 노드 -> 일단 무조건 얼리어답터
for i, node in enumerate(tree):
    if len(node) == 0:
        early[parents[i]] = True

# 2. dfs 돌려서 연결된 모든 노드가 early다? -> 본인은 early일 필요 X
for i, node in enumerate(tree):
    cond = True
    for v in node:
        if early[v] == False:
            cond = False
            early[i] = True
    if cond:
        early[i] = False


t, f = 0, 0
for V in early:
    if V == True:
        t += 1
    else:
        f += 1

answer = min(t, f)
print(answer)
