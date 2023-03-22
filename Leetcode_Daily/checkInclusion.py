import typing


# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         import itertools
#         permutation = itertools.permutations(s1)
#         ls = list()
#         for tup in permutation:
#             ls.append("".join(tup))
#         for i in ls:
#             if i in s2:
#                 return True
#         return False

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1count = [0] * 26
        s2count = [0] * 26
        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord('a')] += 1
            s2count[ord(s2[i]) - ord('a')] += 1
        matches = 0
        for i in range(26):
            matches += (1 if s1count[i] == s2count[i] else 0)
        l = 0
        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True
            idx = ord(s2[i]) - ord("a")
            s2count[idx] += 1
            if s1count[idx] == s2count[idx]:
                matches += 1
            elif s1count[idx] + 1 == s2count[idx]:
                matches -= 1

            idx = ord(s2[l]) - ord("a")
            s2count[idx] -= 1

            if s1count[idx] == s2count[idx]:
                matches += 1
            elif s1count[idx] - 1 == s2count[idx]:
                matches -= 1
            l += 1
        return matches == 26
