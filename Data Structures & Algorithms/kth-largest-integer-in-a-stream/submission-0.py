class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [-n for n in nums]
        heapq.heapify(self.heap)
        self.find = k

    def getKth(self, k):
        copy = self.heap.copy()
        for _ in range(k):
           result = heapq.heappop(copy)
        return result

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)

        
        return - self.getKth(self.find)

        
