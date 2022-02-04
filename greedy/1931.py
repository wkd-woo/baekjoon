N = int(input())
meetings = []

for i in range(N):
    insert = list(map(int, input().split()))
    if 0 <= insert[0] <= insert[1]:
        meetings.append(insert)

if 1 <= N <= 100000:
    meetings = sorted(meetings)
    schedule = []

    for meeting in meetings:
        if len(schedule) == 0:
            schedule.append(meeting)
        else:
            if meeting[1] < schedule[-1][1]:
                schedule.pop()
                schedule.append(meeting)
            elif meeting[0] == schedule[-1][1]:
                schedule.append(meeting)
            elif meeting[0] >= schedule[-1][1]:
                schedule.append(meeting)
            else:
                pass

    print(len(schedule))
