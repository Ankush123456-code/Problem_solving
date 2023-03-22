from collections import defaultdict
from typing import List


class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hm = defaultdict(int)
        for index, value in enumerate(nums):
            hm[value] = index
        res = [i for i in nums]
        for i in operations:
            op1 = i[0]
            op2 = i[1]
            res[hm[op1]] = op2
            hm[op2] = hm[op1]
        return res
