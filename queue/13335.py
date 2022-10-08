from collections import deque


n, w, l = map(int, input().split())  # w:다리의 길이, l: 최대하중
a = deque(map(int, input().split()))

t, passed = 1, 0
bridge, bridge_time = deque([a.popleft()]), deque([1])

while passed < n:
    t += 1
    for i, bt in enumerate(bridge_time):
        bridge_time[i] += 1

    while bridge_time and bridge_time[0] > w:
        bridge.popleft()
        bridge_time.popleft()
        passed += 1

    if a and sum(bridge) + a[0] <= l:
        bridge.append(a.popleft())
        bridge_time.append(1)

print(t)
