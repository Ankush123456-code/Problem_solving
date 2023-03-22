class Solution:
    def capitalizeTitle(self, title: str) -> str:
        if len(title) == 1 or len(title) == 2:
            return title.lower()
        tit = title.split()
        ans = []
        for word in tit:
            i = 0
            word[i] = word[i].upper()
            i += 1
            while i < len(word):
                word[i] = word[i].lower()
                i += 1
            ans.append(word)
        return " ".join(ans)
