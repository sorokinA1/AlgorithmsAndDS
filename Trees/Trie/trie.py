# https://www.youtube.com/watch?v=oobqoCJlHA0
class TrieNode:
    def __init__(self):
        self.children = { }
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        cur_node = self.root

        for char in word:
            if char not in cur_node.children:
                cur_node.children[char] = TrieNode()
            cur_node = cur_node.children[char]
        cur_node.end = True

    def search(self, word: str) -> bool:
        cur_node = self.root

        for char in word:
            if char not in cur_node.children:
                return False
            cur_node = cur_node.children[char]
        return cur_node.end  # check if set to true

    def starts_with(self, prefix: str) -> bool:
        cur_node = self.root

        for char in prefix:
            if char not in cur_node.children:
                return False
            cur_node = cur_node.children[char]
        return True


trie = Trie()
trie.insert('ape')
trie.insert('apple')

# print(trie.search('ape'))
# print(trie.search('app'))
# print(trie.search('apple'))

print(trie.starts_with('ape'))
print(trie.starts_with('ap'))
