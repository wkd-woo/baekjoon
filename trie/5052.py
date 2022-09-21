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

    def search(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                return False
            else:
                current_node = current_node.children[char]

        if current_node.children:
            return False
        return True

    def starts_with(self, prefix):
        current_node = self.head
        words = []

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return None

        current_node = [current_node]
        next_node = []
        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break

        return words


for _ in range(int(input())):
    n = int(input())
    trie = Trie()
    l = [input().replace(' ', '') for _ in range(n)]
    for each in l:
        trie.insert(each)
    cnd = True
    for each in l:
        if len(trie.starts_with(each)) > 1:
            print("NO")
            cnd = False
            break
    if cnd:
        print("YES")