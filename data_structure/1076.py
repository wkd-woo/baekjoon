color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

db = {c: [i, 10 ** i] for i, c in enumerate(color)}
one = input()
two = input()
three = input()

print((db[one][0] * 10 + db[two][0]) * db[three][1])