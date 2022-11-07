from collections import defaultdict


n = int(input())
db = defaultdict(int)
mx, answer = 9, 0
words = [list(input()) for _ in range(n)]

for word in words:
    for i, each in enumerate(word):
        db[each] += 10**(len(word) - i - 1)

for K, V in sorted(db.items(), key=lambda x: -x[1]):
    answer += V * mx
    mx -= 1

print(answer)
