class Solution:
    def canJump(self, nums: List[int]) -> bool:

        last = len(nums) - 1

        max_jump = nums[0]

        index = 0

        while max_jump > 0 and index < last:
            index += 1
            max_jump -= 1

            max_jump = max(max_jump, nums[index])
        
        return index >= last

        



