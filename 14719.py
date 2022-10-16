h, w = map(int, input().split())
blocks = list(map(int, input().split()))

left = [-int(1e9)] * (w+1)
for i in range(1, w):
    left[i] = max(left[i-1], blocks[i-1])

right = -int(1e9)
answer = 0
for i in range(w-2, 0, -1):
    right = max(right, blocks[i+1])

    if (min(left[i], right) > blocks[i]):
        answer += min(left[i], right) - blocks[i]

print(answer)
