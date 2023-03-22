class Solution:
    def partition(self, s: str):
        res = []

        def is_palindrome(strr):
            start = 0
            end = len(strr) - 1
            while start < end:
                if strr[start] != strr[end]:
                    return False
                start += 1
                end -= 1
            return True

        def dfs(index, temp):
            if index == len(s):
                res.append(temp.copy())
                return
            else:
                for i in range(index, len(s)):
                    if is_palindrome(s[index:i + 1]):
                        temp.append(s[index:i + 1])
                        dfs(i + 1, temp)
                        temp.pop()
                return

        dfs(0, [])
        return res
