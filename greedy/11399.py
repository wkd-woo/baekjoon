n = int(input())

people = sorted(map(int, input().split()))

total = []
for person in people:
    if not total:
        total.append(person)
    else:
        total.append(person + total[-1])

print(sum(total))
