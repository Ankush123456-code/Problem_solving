class Solution:
    def findJudge(self, n: int, trust):
        ind = [0] * (n + 1)
        out = [0] * (n + 1)
        for i in trust:
            ind[i[0]] += 1
            out[i[1]] += 1

        for i in range(1, n + 1):
            if ind[i] == 0 and out[i] == n - 1:
                return i
        return -1
