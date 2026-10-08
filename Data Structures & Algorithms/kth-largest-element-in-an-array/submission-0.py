class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        self.heap = nums
        heapq.heapify(self.heap)

        self.k = k

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]