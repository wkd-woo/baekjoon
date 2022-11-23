
while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break

    l = list(map(int, input().split()))
    tree = dict()
    stack = []
    for i, each in enumerate(l):
        if i == 0:
            tree[each] = []
            continue

        if not stack:
