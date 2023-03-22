import heapq
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = nums
        heapq.heapify(heap)
        res = []
        while heap:
            res.append(heapq.heappop(heap))
        return res
