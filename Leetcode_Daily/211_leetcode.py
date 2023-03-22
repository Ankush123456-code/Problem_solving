# import collections
#
# Giving time_complexity error so znd method is use trie istead of hashing
# class WordDictionary:
#
#     def __init__(self):
#         self.wd = collections.defaultdict(list)
#
#     def addWord(self, word: str) -> None:
#         sz = len(word)
#         if sz in self.wd:
#             self.wd[sz].append(word)
#         else:
#             self.wd[sz].append(word)
#
#     def search(self, word: str) -> bool:
#         c = 0
#         for i in word:
#             if i.isalpha():
#                 c += 1
#         ans = 0
#         if len(word) in self.wd:
#             words = self.wd[len(word)]
#             for wd in words:
#                 temp = 0
#                 for i in range(len(wd)):
#                     if word[i] == wd[i] and word[i] != '.':
#                         temp += 1
#                 ans = max(temp, ans)
#             if ans == c:
#                 return True
#             else:
#                 return False
#         return False

class Trie:
    def __init__(self):
        self.child = [None for i in range(256)]
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        root = self.trie
        for ch in word:
            id = ord(ch) - ord('a')
            # print(id)
            if root.child[id] is None:
                root.child[id] = Trie()
            root = root.child[id]
        root.isEnd = True

    def search(self, word: str) -> bool:

        def dfs(word, root):
            for i in range(len(word)):
                if word[i] == '.':
                    for c in root.child:
                        if c and dfs(word[i + 1:], root):
                            return True
                    return False
                id = ord(word[i]) - ord('a')
                if root.child[id] is None:
                    return False
                root = root.child[id]
            return root.isEnd

        root = self.trie
        search_word = word
        return dfs(search_word, root)
# strr="Ankush"
# print((strr[1:]))