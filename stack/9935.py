l = list(input())
word = input()
stack = []

for w in l:
    if w == word:
        continue
    if not stack:
        stack.append(w)
    elif ''.join(stack[-len(word)+1:] + [w]) == word:
        for _ in range(len(word)-1):
            stack.pop()
    else:
        stack.append(w)

if stack:
    print(''.join(stack))
else:
    print("FRULA")
