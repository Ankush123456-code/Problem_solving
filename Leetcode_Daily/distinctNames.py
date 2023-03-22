import collections


class Solution:
    def distinctNames(self, ideas) -> int:
        word_map = collections.defaultdict(set)
        for word in ideas:
            word_map[word[0]].add(word[1:])

        res = 0
        for char in word_map:
            for char2 in word_map:
                if char == char2:
                    continue
                intersect = 0
                for w in word_map[char]:
                    if w in word_map[char2]:
                        intersect += 1
                dis1 = len(word_map[char]) - intersect
                dis2 = len(word_map[char2]) - intersect
                res += dis1 * dis2
        return res
