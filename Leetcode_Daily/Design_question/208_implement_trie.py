class TrieNode:
    def __init__(self):
        self.child = {}
        self.end_of_word = False


class Trie:

    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        root = self.trie
        for ch in word:
            if ch not in root.child:
                root.child = Trie()
            root = root.child[ch]
        root.isEnd = True

    def search(self, word: str) -> bool:
        root = self.trie
        for ch in word:
            if ch not in root.child:
                return False
            root = root.child[ch]
        return root.isEnd

    def startsWith(self, prefix: str) -> bool:
        root = self.trie
        for ch in prefix:
            if ch not in root.child:
                return False
            root = root.child[ch]
        return True
