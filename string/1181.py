n = int(input())
answer = sorted(set(input() for _ in range(n)))
answer.sort(key=lambda x: (len(x), x))
for each in answer:
    print(each)