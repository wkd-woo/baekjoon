s = input()
answer = 0
for each in ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']:
    answer += s.count(each)
    s = s.replace(each, ' ')

print(answer + len(s.replace(' ', '')))