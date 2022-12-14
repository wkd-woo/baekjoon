from queue import PriorityQueue


n, m = map(int, input().split())
l = list(map(int, input().split()))
w = list(map(int, input().split()))

cond = 1
que = PriorityQueue()
for i, each in enumerate(l):
    que.put((-each, i+1))

for i, child in enumerate(w):
    gifts, idx = que.get()
    gifts = -gifts
    if gifts >= child:
        gifts -= child
        que.put((-gifts, idx))

    else:
        cond = 0
        break


print(cond)
