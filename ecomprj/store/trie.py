from collections import defaultdict
class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.is_end_of_word = False

    def search(self, word):
        current = self
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def insert(self, word):
        current = self
        for char in word:
            current = current.children[char]
        current.is_end_of_word = True
