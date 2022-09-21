class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string

    def starts_with(self, prefix):
        current_node = self.head

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return None

        return True


N, M = map(int, input().split())
l = [input() for _ in range(N)]
prefix = [input() for _ in range(M)]

trie = Trie()
for each in l:
    trie.insert(each)

answer = 0
for p in prefix:
    if trie.starts_with(p):
        answer += 1

print(answer)