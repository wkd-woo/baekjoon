from collections import defaultdict

s = list(input())
db = defaultdict(int)

for w in s:
    db[w.upper()] += 1

mx = 0
answer = []
for K, V in db.items():
    if V > mx:
        mx = V
        answer = [K]
    elif V == mx:
        answer.append(K)

if len(answer) == 1:
    print(answer[0])
else:
    print('?')