n = int(input())
l = [tuple(map(int, input().split())) for _ in range(n)]

answer = []
for i in l:
    rank = 1
    for j in l:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    answer.append(rank)

print(*answer)
