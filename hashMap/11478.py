s = list(input())

db = set()
for i in range(len(s)):
    for j in range(len(s)):
        db.add(''.join(s[i:i+j+1]))

print(len(db))
