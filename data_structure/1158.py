n, k = map(int, input().split())
queue = [i for i in range(1, n + 1)]
result = []
index = 0

while queue:
    index = (index + (k - 1)) % len(queue)
    result.append(queue.pop(index))

print("<", ", ".join(map(str, result)), ">", sep='')