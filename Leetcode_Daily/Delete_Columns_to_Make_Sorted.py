class Solution:
    def minDeletionSize(self, strs):
        res = 0
        for j in range(len(strs[0])):
            for i in range(len(strs) - 1):
                if strs[i][j] > strs[i + 1][j]:
                    res += 1
                    break

        return res
