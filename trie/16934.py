from collections import defaultdict


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
        nickname = ''
        for i, char in enumerate(string):
            if char not in current_node.children:
                if not nickname:
                    nickname = string[:i + 1]
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string
        return nickname


N = int(input())
l = [input() for _ in range(N)]
trie = Trie()
db = defaultdict(int)
alias = []
for nic in l:
    temp = trie.insert(nic)
    db[nic] += 1
    if not temp and db:
        if db[nic] != 1:
            temp = nic + str(db[nic])
        else:
            temp = nic
    alias.append(temp)

print('\n'.join(alias))