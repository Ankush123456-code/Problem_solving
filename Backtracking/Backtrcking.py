class Solution:
    def restoreIpAddresses(self, s: str):
        res = []
        if len(s) > 12:
            return res

        def dfs(ps, temp):
            if ps == len(s) and len(temp) == 4:
                res.append(".".join(temp))
                return
            if len(temp) == 4:
                return
            for i in range(1, 4):
                if ps + i > len(s):
                    break
                if int(s[ps:ps+i]) > 255:
                    continue
                if i > 1 and s[ps] == 0:
                    continue
                dfs(ps + i,  temp+[s[ps:ps + i]])

        dfs(0, [])
        return res

