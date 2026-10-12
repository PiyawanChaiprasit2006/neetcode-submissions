class Solution:
    def trap(self, height: List[int]) -> int:
        
        # 
        
        left = 0
        right = len(height) -1

        water = max_left = max_right = 0

        while left < right:
            if height[left] < height[right]:
                max_left = max(height[left], max_left)
                water += max_left - height[left]
                left += 1
            else:
                max_right = max(height[right], max_right)
                water += max_right - height[right]
                right -= 1

        return water
        
            

            