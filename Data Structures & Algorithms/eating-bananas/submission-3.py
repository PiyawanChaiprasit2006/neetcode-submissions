class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)

        mid = (left + right) // 2

        k = max(piles)

        while left <= right:
            
            hours = 0
            for pile in piles:
                if (pile // mid == 0):
                    hours += 1
                else:
                    hours += math.ceil(pile / mid)

            if hours > h:
                left = mid + 1
            else:
                right = mid - 1
                k = min(k, mid)

            
            mid = (left + right) // 2
        
        return k
                

