T = int(input())
button = [300, 60, 10]
cnt = []

for each in button:
    next_ = T // each
    T -= each * next_
    cnt.append(next_)

print(*cnt) if T == 0 else print(-1)
