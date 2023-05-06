import collections


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        r = collections.deque()
        d = collections.deque()
        for idx, val in enumerate(str):
            if val == "R":
                r.append(idx)
            else:
                d.append(idx)
        while r and d:
            ridx = r.popleft()
            didx = d.popleft()
            if ridx < didx:
                ridx = ridx + len(senate)
                r.append(ridx)
            else:
                didx = didx + len(senate)
                d.append(didx)
        return "Radiant" if r else "Dire"
