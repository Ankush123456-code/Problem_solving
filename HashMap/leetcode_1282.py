from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hm = defaultdict(list)
        for index, value in enumerate(groupSizes):
            hm[value].append(index)

        res = []
        for key, value in hm.items():
            while value:
                ans = []
                for i in range(key):
                    ans.append(value.pop())
                res.append(ans)
        return res
