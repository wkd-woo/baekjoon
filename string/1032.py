N = int(input())
l = [input() for _ in range(N)]
word_len = len(l[0])
answer = ''
for i in range(word_len):
    db = set()
    for word in l:
        db.add(word[i])

    if len(db) == 1:
        answer = answer + l[0][i]
    else:
        answer = answer + '?'

print(answer)