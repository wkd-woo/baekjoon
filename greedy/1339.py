from collections import defaultdict, deque


n = int(input())
db, mx, answer = defaultdict(int), 9, 0
words_org = [input() for _ in range(n)]
words = [deque(word) for word in words_org]

while words:
    words.sort(key=lambda x: len(x))
    word = words.pop()
    alpha = word.popleft()
    if words_org.count(''.join(word)) == len(words) and alpha not in db:
        db[alpha] = mx - 1

    if alpha not in db:
        db[alpha] = mx
        mx = min(db.values()) - 1
    answer += (10 ** (len(word))) * db[alpha]
    if word:
        words.append(word)

print(answer)
