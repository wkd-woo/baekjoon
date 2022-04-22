n = int(input())
p = list(map(int, input().split()))
d = int(input())
tree = {}

for i in range(n):
    if i == d or p[i] == d:
        continue
    if p[i] in tree: # 부모노드에 자식 연관관계 추가
        tree[p[i]].append(i)
    else:
        tree[p[i]] = [i]

res = 0

if -1 in tree: # 루트 노드 설정
    q = [-1]
else:
    q = []

while q:
    node = q.pop()
    if node not in tree:
        res += 1
    else:
        q += tree[node]

print(res)