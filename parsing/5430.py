from collections import deque

for _ in range(int(input())):
    cmd = deque(input())
    n = int(input())
    l = input().strip('['']')
    if n == 0 and 'D' in cmd:
        print("error")
        continue


    l = deque(l.split(','))
    if '' in l:
        l.remove('')
    reverse_cnd = False
    print_cnd = True
    while cmd:
        c = cmd.popleft()
        if c == 'R':
            reverse_cnd = not reverse_cnd
        elif c == 'D' and l:
            if reverse_cnd:
                l.pop()
            if not reverse_cnd:
                l.popleft()
        elif c == 'D' and not l:
            print("error")
            print_cnd = False
            break

    if print_cnd:
        if not reverse_cnd:
            print('[' + ','.join(l) + ']')
        else:
            print('[' + ','.join(reversed(l)) + ']')