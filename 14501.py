N = int(input())
consultations = []
money = 0

for i in range(N):
    consultations.append(list(map(int, input().split())))

if 1 <= N <= 15:
    schedule = []

    for i, consultation in enumerate(consultations):
        if i + consultation[0] <= N:
            schedule.append([i + 1] + [i + consultation[0]] + [consultation[1]])

    for i in range(len(schedule)):
        temp = 0
        for j in range(i, schedule[i][1]):
            if j <= len(schedule):
                temp += schedule[j - 1][2]
            if schedule[i][2] >= temp:
                money += schedule[i][2]

print(money)
