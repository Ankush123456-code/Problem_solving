import heapq


class SeatManager:

    def __init__(self, n: int):
        self.min_heap = [i for i in range(1, n + 1)]

    def reserve(self) -> int:
        import heapq
        return heapq.heappop(self.min_heap)

    def unreserve(self, seatNumber: int) -> None:
        import heapq
        heapq.heappush(self.min_heap, seatNumber)
